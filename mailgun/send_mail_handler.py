import smtplib
import json
from email.message import EmailMessage
from khayyam import JalaliDatetime

from mailgun.config import info_mail
from config import rules


def send_mail(rates):
    """
    get receive_time and rates, check if there is preferred rates and
    then send email through smtp
    :param receive_time:
    :param rates:
    :return:
    """
    preferred = rules["mail"]["preferred"]
    subject = f"{JalaliDatetime.now().strftime('%Y-%m-%d %H:%M')} rates"
    if preferred is not None:
        rates = {i: rates[i] for i in preferred if i in rates.keys()}

    text = json.dumps(rates)

    send_smtp_email(subject, text)


def send_smtp_email(subject, body):
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = info_mail["sender"]
    msg["To"] = info_mail["receiver"]
    msg.set_content(body)

    with smtplib.SMTP_SSL(info_mail["smtp_server"], info_mail["port"]) as server:
        try:
            server.login(info_mail["sender"], info_mail["password"])
            server.send_message(msg)
            print("Email was sent successfully.")
        except smtplib.SMTPAuthenticationError as e:
            print(f"satus code is [{e.smtp_code}]\n"
                  f"Username and Password not accepted.")
        except smtplib.SMTPException as e:
            print(e)
