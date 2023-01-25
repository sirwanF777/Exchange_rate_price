import smtplib
from config import info_mail

from email.message import EmailMessage


def sand_smtp_email(subject, body):
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = info_mail["sender"]
    msg["To"] = info_mail["receiver"]
    msg.set_content(body)

    with smtplib.SMTP_SSL(info_mail["smtp_server"], info_mail["port"]) as server:
        server.login(info_mail["sender"], info_mail["password"])
        server.send_message(msg)
