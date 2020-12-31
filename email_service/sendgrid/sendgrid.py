import base64

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import (
    Attachment,
    Bcc,
    Cc,
    Content,
    Disposition,
    FileContent,
    FileName,
    FileType,
    From,
    Mail,
    MimeType,
    ReplyTo,
    Subject,
    To,
)

from email_service.utils.clean_data import CleanData
from email_service.utils.constants import ATTACHMENT_FILE_TYPES
from email_service.utils.functions import read_file_in_binary
from email_service.utils.validators import Validation


class SendgridMail:
    """To send the email using sendgrid"""

    def __init__(self, api_key: str):
        self.SENDGRID_API_KEY = api_key

    def add_attachment(self, data):
        attached_files = []
        for single_file in data:
            disposition = "attachment"
            single_file = single_file

            extension = single_file.split(".")[-1]
            file_type = ATTACHMENT_FILE_TYPES[extension]

            binary_content = read_file_in_binary(single_file)
            encoded = base64.b64encode(binary_content).decode()

            attachment = Attachment()
            attachment.file_content = FileContent(encoded)
            attachment.file_type = FileType(file_type)
            attachment.file_name = FileName(single_file)
            attachment.disposition = Disposition(disposition)

            attached_files.append(attachment)
        return attached_files

    def form_message(
        self,
        sub="Default Subject",
        reply_to_addresses=[],
        html_body=None,
        text_body=None,
        to=[],
        from_email=None,
        cc=[],
        bcc=[],
        attachments=[],
    ):
        """Forming the mail to be send"""

        message = Mail()
        message.to = [To(emails.get("email"), emails.get("name")) for emails in to]
        message.cc = [Cc(emails.get("email"), emails.get("name")) for emails in cc]
        message.bcc = [Bcc(emails.get("email"), emails.get("name")) for emails in bcc]
        message.subject = Subject(sub)
        message.from_email = From(from_email)
        message.reply_to = ReplyTo(
            None if not reply_to_addresses else reply_to_addresses[0]
        )  # reply_to take only one entry in case of sendgrid
        if text_body:
            message.content = Content(MimeType.text, text_body)
        if html_body:
            message.content = Content(MimeType.html, html_body)

        if attachments:
            message.attachment = self.add_attachment(attachments)
        return message

    def send_email(self, message) -> dict:
        try:
            sg = SendGridAPIClient(self.SENDGRID_API_KEY)
            response = sg.send(message)
            return {
                "status_code": response.status_code,
                "message": f"{response.body}",
            }
        except Exception as e:
            # For accepting HttpError
            try:
                status = {
                    "status_code": e.status_code,
                    "message": f"{e.body}",
                }

            # For accepting Other errors
            except Exception:
                status = {
                    "status_code": 400,
                    "message": "Something Went Wrong",
                }
            return status

    def bulk(self, data: dict) -> dict:
        """
        Bulk Email : Email will be sent in a bulk of (500 for sendgrid) including all the to, cc, bcc
        :param data:
        :return:
        """

        # Cleaning the data
        event = CleanData().clean_data(data)

        # For returning Status
        status = dict()

        # For sending Bulk Mail
        event["receipients"]["bcc"].extend(event["receipients"]["to"])
        event["receipients"]["to"] = None
        cc_count = len(event["receipients"]["cc"])
        bcc_count = len(event["receipients"]["bcc"])
        batch = 500 - cc_count - 1  # -1 for 'to' email
        for emails in range(0, bcc_count, batch):
            message = self.form_message(
                sub=event["subject"],
                reply_to_addresses=event["reply_to_addresses"],
                html_body=event["html_body"],
                text_body=event["text_body"],
                from_email=event["from_email"],
                to=event["to_for_bulk"],
                cc=event["receipients"]["cc"],
                bcc=event["receipients"]["bcc"][emails : emails + batch],
                attachments=event["attachments"],
            )
            status = self.send_email(message)

        return status

    def individual(self, data) -> dict:
        """
        Individual Email : All the emails will be sent separately, if mentioned in to and
            cc,bcc will be attached with all the emails
        :param data:
        :return status:
        """
        # Cleaning the data
        event = CleanData().clean_data(data)

        # Storing Status
        status = dict()

        # Sending Individual Mail
        for email_id in event["receipients"]["to"]:
            message = self.form_message(
                sub=event["subject"],
                reply_to_addresses=event["reply_to_addresses"],
                html_body=event["html_body"],
                text_body=event["text_body"],
                to=[email_id],
                from_email=event["from_email"],
                cc=event["receipients"]["cc"],
                bcc=event["receipients"]["bcc"],
                attachments=event["attachments"],
            )
            status = self.send_email(message)
        return status

    def sendgrid_handler(self, data: dict, email_type="INDIVIDUAL") -> dict:
        validation = Validation().validation(data)

        if "attachments" in data.keys() and len(data["attachments"]) > 0:
            Validation().file_existnece(data["attachments"])

        if validation["status_code"] == 200:
            status = dict()
            if email_type == "INDIVIDUAL":
                status = self.individual(data)
            else:
                status = self.bulk(data)
            return status
        else:
            return validation
