import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import boto3
from botocore.exceptions import ClientError

from email_service.utils.clean_data import CleanMailingList
from email_service.utils.constants import ATTACHMENT_FILE_TYPES
from email_service.utils.functions import read_file_in_binary
from email_service.utils.validators import Validation


class SESMail:
    """To send the email using AWS SES"""

    def __init__(self, aws_access_key_id: str, aws_secret_access_key: str, aws_region: str, charset: str,
                 smtp_host, port, smtp: bool = True) -> None:
        self.AWS_ACCESS_KEY_ID = aws_access_key_id
        self.AWS_SECRET_ACCESS_KEY = aws_secret_access_key
        self.AWS_REGION = aws_region
        self.CHARSET = charset
        self.SMTP = smtp
        self.SMTP_HOST = smtp_host
        self.PORT = port

    @staticmethod
    def add_attachment(data: list) -> list:
        attached_files = []
        for single_file in data:
            disposition = "attachment"
            single_file = single_file

            file_name, extension = single_file.split(".")
            file_type = ATTACHMENT_FILE_TYPES[extension]

            binary_content = read_file_in_binary(single_file)

            attachment = MIMEApplication(binary_content)
            attachment.add_header('Content-Disposition', disposition, filename=f"{file_name}.{extension}")

            attached_files.append(attachment)
        return attached_files

    def form_message(
        self,
        sub: str = "Default Subject",
        reply_to_addresses=None,
        html_body: str = None,
        text_body=None,
        to=None,
        from_email=None,
        cc=None,
        bcc=None,
        attachments=None,
        return_path_address: str = None
    ):
        """Forming the mail to be send"""
        # Handle the default values of params
        if attachments is None:
            attachments = []
        if bcc is None:
            bcc = []
        if cc is None:
            cc = []
        if to is None:
            to = []
        if reply_to_addresses is None:
            reply_to_addresses = []

        message = MIMEMultipart("mixed")
        message["To"] = ", ".join([f"{emails.get('name')} <{emails.get('email')}>" for emails in to])
        message["Cc"] = ", ".join([f"{emails.get('name')} <{emails.get('email')}>" for emails in cc])
        message["Bcc"] = ", ".join([f"{emails.get('name')} <{emails.get('email')}>" for emails in bcc])
        message["Subject"] = sub
        message["From"] = from_email
        if reply_to_addresses:
            message['Reply-To'] = reply_to_addresses[0]
        if return_path_address:
            message["Return-Path"] = return_path_address

        message_subtype = "alternative" if text_body and html_body else "mixed"
        message_body = MIMEMultipart(message_subtype)

        if text_body:
            text_body_content = MIMEText(text_body.encode(self.CHARSET), "plain", self.CHARSET)
            message_body.attach(text_body_content)
        if html_body:
            html_body_content = MIMEText(html_body.encode(self.CHARSET), "html", self.CHARSET)
            message_body.attach(html_body_content)
        message.attach(message_body)

        if attachments:
            attachments_list = self.add_attachment(attachments)
            for attachment in attachments_list:
                message.attach(attachment)

        return message

    def send_email(self, message, sender: str, recipients: list) -> dict:
        try:
            if self.SMTP:
                server = smtplib.SMTP(host=self.SMTP_HOST, port=self.PORT)
                server.ehlo()
                server.starttls()
                # stmplib docs recommend calling ehlo() before & after starttls()
                server.ehlo()

                server.login(self.AWS_ACCESS_KEY_ID, self.AWS_SECRET_ACCESS_KEY)

                response = server.sendmail(
                    sender,
                    ", ".join([f"{email_dict.get('name')} <{email_dict.get('email')}>" for email_dict in recipients]),
                    message.as_string())
                server.close()

                return {
                    "status_code": 202,
                    "message": f"{response}",
                }

            else:
                client = boto3.client('ses',
                                      aws_access_key_id=self.AWS_ACCESS_KEY_ID,
                                      aws_secret_access_key=self.AWS_SECRET_ACCESS_KEY,
                                      region_name=self.AWS_REGION)
                response = client.send_raw_email(
                    Source=sender,
                    Destinations=[email_dict.get("email") for email_dict in recipients],
                    RawMessage={
                        'Data': message.as_string(),
                    }
                )

                return {
                    "status_code": 202,
                    "message": f"{response['MessageId']}",
                }
        except ClientError as e:
            return {
                "status_code": 400,
                "message": f"{e.response['Error']['Message']}",
            }
        except Exception as e:
            status = {
                "status_code": 400,
                "message": f"Something Went Wrong: {e}",
            }
            return status

    def bulk(self, data: dict) -> dict:
        """
        Bulk Email : Email will be sent in a bulk of (500 for sendgrid) including all the to, cc, bcc
        :param data:
        :return:
        """

        # Cleaning the data
        event = CleanMailingList().clean_mailing_list(data)

        # For returning Status
        status = dict()

        # For sending Bulk Mail
        event["recipients"]["bcc"].extend(event["recipients"]["to"])
        event["recipients"]["to"] = None
        cc_count = len(event["recipients"]["cc"])
        bcc_count = len(event["recipients"]["bcc"])
        batch = 500 - cc_count - 1  # -1 for 'to' email
        for emails in range(0, bcc_count, batch):
            message = self.form_message(
                sub=event["subject"],
                reply_to_addresses=event["reply_to_addresses"],
                html_body=event["html_body"],
                text_body=event["text_body"],
                from_email=event["from_email"],
                to=event["to_for_bulk"],
                cc=event["recipients"]["cc"],
                bcc=event["recipients"]["bcc"][emails: emails + batch],
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
        event = CleanMailingList().clean_mailing_list(data)

        # Storing Status
        status = dict()

        # Sending Individual Mail
        for email_id in event["recipients"]["to"]:
            message = self.form_message(
                sub=event["subject"],
                reply_to_addresses=event["reply_to_addresses"],
                html_body=event["html_body"],
                text_body=event["text_body"],
                to=[email_id],
                from_email=event["from_email"],
                cc=event["recipients"]["cc"],
                bcc=event["recipients"]["bcc"],
                attachments=event["attachments"],
                return_path_address=event["return_path_address"]
            )
            status = self.send_email(message, event["from_email"], [email_id])
        return status

    def ses_handler(self, data: dict, email_type="INDIVIDUAL") -> dict:
        validation = Validation().validation(data)

        if "attachments" in data.keys() and len(data["attachments"]) > 0:
            Validation().file_existence(data["attachments"])

        if validation["status_code"] == 200:
            status = dict()
            if email_type == "INDIVIDUAL":
                status = self.individual(data)
            else:
                status = self.bulk(data)
            return status
        else:
            return validation
