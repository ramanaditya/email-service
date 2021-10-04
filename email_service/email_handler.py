from email_service.settings import Settings
from email_service.utils import constants


class EmailHandler:
    def __init__(self, email_type="INDIVIDUAL") -> None:
        self.EMAIL_TYPE = email_type
        if not self.EMAIL_TYPE.upper() in constants.AVAILABLE_EMAIL_TYPES:
            raise ValueError("Invalid Email type is passed")

    def sendgrid(self, data: dict, api_key=None) -> dict:
        from email_service.sendgrid.sendgrid import SendgridMail

        API_KEY = Settings().SENDGRID_API_KEY or api_key
        if not API_KEY:
            raise KeyError("SENDGRID_API_KEY not found in environment")
        sendgrid_mail = SendgridMail(API_KEY)
        response = sendgrid_mail.sendgrid_handler(data, email_type=self.EMAIL_TYPE)
        return response

    def aws_ses(self, data: dict, aws_access_key_id: str = None, aws_secret_access_key: str = None,
                aws_region: str = None, smtp_host: str = None, port: str = None, charset: str = None) -> dict:
        from email_service.ses.aws_ses import SESMail

        aws_access_key_id = Settings().AWS_ACCESS_KEY_ID or aws_access_key_id
        aws_secret_access_key = Settings().AWS_SECRET_ACCESS_KEY or aws_secret_access_key
        smtp_host = Settings().SMTP_HOST or smtp_host
        port = Settings().PORT or port
        aws_region = Settings().AWS_REGION or aws_region
        charset = charset or Settings().CHARSET
        if not aws_access_key_id or not aws_secret_access_key or not aws_region:
            raise KeyError("AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_REGION not found")
        ses_mail = SESMail(aws_access_key_id, aws_secret_access_key, aws_region, charset, smtp_host, port)
        response = ses_mail.ses_handler(data, email_type=self.EMAIL_TYPE)
        return response
