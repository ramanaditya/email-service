import os


class Settings:
    CHARSET = None
    SENDGRID_API_KEY = None

    def __init__(self):
        self.CHARSET = os.environ.get("CHARSET", default="utf-8")
        self.SENDGRID_API_KEY = os.environ.get("SENDGRID_API_KEY")
