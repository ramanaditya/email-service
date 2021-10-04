import os


class Settings:
    def __init__(self):
        self.CHARSET = os.environ.get("CHARSET", default="utf-8")
        self.SENDGRID_API_KEY = os.environ.get("SENDGRID_API_KEY")
        self.AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
        self.AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
        self.AWS_REGION = os.environ.get("AWS_REGION")
        self.SMTP_HOST = os.environ.get("SMTP_HOST")
        self.PORT = os.environ.get("PORT")
