from email_service.email_handler import EmailHandler

data = {
    "subject": "This is the test for the Individual email",
    "reply_to_addresses": "email1@gmail.com",  # string
    "html_body": "<h1>Email Template for Individual email</h1>",
    "text_body": "Email Template for Individual email",
    "from_email": "Name WithSpace <from_email@gmail.com>",
    "to_for_bulk": [{"name": "Name", "email": "email@gmail.com"},],
    "recipients": {
        "to": [{"name": "name1", "email": "email1@gmail.com"},],
        "cc": [{"name": "name2", "email": "email2@google.com"},],
        "bcc": [{"name": "name3", "email": "email3@google.com"},],
    },
    "attachments": [
        "file_path (pdf)",
        "calender invite (ics)",
        "image_path (png/jpg/jpeg)",
    ],
}

send_email = EmailHandler(email_type="BULK")
response = send_email.sendgrid(data)
print(response)
