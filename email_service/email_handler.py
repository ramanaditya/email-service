from email_service.sendgrid.sendgrid import SendgridMail
from email_service.settings import Settings
from email_service.utils import constants


class EmailHandler:
    def __init__(self, email_type="INDIVIDUAL") -> None:
        self.EMAIL_TYPE = email_type
        if not self.EMAIL_TYPE.upper() in constants.AVAILABLE_EMAIL_TYPES:
            raise ValueError("Invalid Email type is passed")

    def sendgrid(self, data: dict, api_key=None) -> dict:
        API_KEY = Settings().SENDGRID_API_KEY or api_key
        if not API_KEY:
            raise KeyError("SENDGRID_API_KEY not found in environment")
        sendgrid_mail = SendgridMail(API_KEY)
        response = sendgrid_mail.sendgrid_handler(data, email_type=self.EMAIL_TYPE)
        return response
