import requests
import json
import os
from datetime import datetime
from khayyam import JalaliDatetime

from config import *
from mail import sand_smtp_email
from notification import send_sms


def get_rates():
    """
    send a get requests to the api.exchangerate.host api and get live rates
    :return:
    """
    response = requests.get(url_free)
    if response.status_code == 200:
        return json.loads(response.text)

    print(f"error\nYour request has encountered status code"
          f" {response.status_code}. Please check")
    return None


def archive(rates):
    """
    add archive folder, get filename and rates, save them to the specific directory
    :param file_name:
    :param rates:
    :return:
    """
    file_name = datetime.now().strftime("%Y-%m-%dT%H.%M.%S")
    if "archive" not in os.listdir():
        directory = "archive"
        parent_dir = os.getcwd()
        path = os.path.join(parent_dir, directory)
        os.mkdir(path)

    with open(f"archive/{file_name.replace(':', '.')}.json", "w") as f:
        f.write(json.dumps(rates))


def send_mail(rates):
    """
    get receive_time and rates, check if there is preferred rates and
    then send email through smtp
    :param receive_time:
    :param rates:
    :return:
    """
    subject = f"{JalaliDatetime.now().strftime('%Y-%m-%d %H:%M')} rates"
    if info_mail["preferred"] is not None:
        rates = {i: rates[i] for i in info_mail["preferred"] if i in rates.keys()}

    text = json.dumps(rates)

    sand_smtp_email(subject, text)


def check_rate_price(rate):
    """
    check if user defined notify rules and if rate reached to the defined
    rules, then generate proper msg to send.
    :param rate:
    :return:mag(str)
    """
    preferred = info_notification["preferred"]
    msg = ""

    for ext in preferred.keys():
        if rate[ext] <= preferred[ext]["min"]:
            msg = str(JalaliDatetime.now().strftime('%Y-%m-%d %H:%M'))
            msg += f"\n{ext} reached min: {rate[ext]}\n"
        elif rate[ext] >= preferred[ext]["max"]:
            msg = str(JalaliDatetime.now().strftime('%Y-%m-%d %H:%M'))
            msg += f"\n{ext} reached max: {rate[ext]}\n"

    return msg


if __name__ == "__main__":
    res = get_rates()

    if rules["archive"]:
        archive(res["rates"])

    if rules["send_mail"]:
        send_mail(res["rates"])

    if rules["send_notification"]:
        notification_msg = check_rate_price(res["rates"])
        if notification_msg:
            send_sms(notification_msg)
