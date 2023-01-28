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
        try:
            server.login(info_mail["sender"], info_mail["password"])
            server.send_message(msg)
        except smtplib.SMTPAuthenticationError as e:
            print(f"satus code is [{e.smtp_code}]\nUsername and Password not accepted.")
        except smtplib.SMTPException as e:
            print(e)
