from email_service.email_handler import EmailHandler

data = {
    "subject": "This is the test for the Individual email",
    "reply_to_addresses": "adtyaraman96@gmail.com",
    "html_body": "<h1>Email Template for Individual email</h1>",
    "text_body": "Email Template for Individual email",
    "from_email": "Aditya Raman <adityaraman96@gmail.com>",
    "receipients": {
        "to": [{"name": "Aditya", "email": "adityaraman1996@gmail.com"},],
        "cc": [{"name": "Raman", "email": "adityaraman_cs004@sirmvit.edu"},],
        "bcc": [
            {"name": "Aditya Raman", "email": "adityaraman@studentambassadors.com"},
        ],
    },
    "attachments": [
        "/Users/aditya/Desktop/microsoft_student_ambassadors.pdf",
        "/Users/aditya/Desktop/invite.ics",
        "/Users/aditya/Desktop/Screenshot 2020-10-22 at 11.55.39 PM.png",
    ],
}

send_email = EmailHandler()
# send_email = EmailHandler(email_type="INDIVIDUAL")    # This is also correct
response = send_email.sendgrid(data)
print(response)
