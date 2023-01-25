import requests
import json
import os
from datetime import datetime

from config import *
from mail import sand_smtp_email


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


def archive(file_name, rates):
    """
    add archive folder, get filename and rates, save them to the specific directory
    :param file_name:
    :param rates:
    :return:
    """
    if "archive" not in os.listdir():
        directory = "archive"
        parent_dir = os.getcwd()
        path = os.path.join(parent_dir, directory)
        os.mkdir(path)

    with open(f"archive/{file_name.replace(':', '.')}.json", "w") as f:
        f.write(json.dumps(rates))


def now_time():
    """
    we get the current date and time using the datetime library
    :return:
    """
    time = f"{datetime.now()}".replace(" ", "T").split(".")[0]
    return time


def send_mail(receive_time, rates):
    """
    get receive_time and rates, check if there is preferred rates and
    then send email through smtp
    :param receive_time:
    :param rates:
    :return:
    """
    subject = f"{receive_time} rates"
    if info_mail["preferred"] is not None:
        rates = {i: rates[i] for i in info_mail["preferred"] if i in rates.keys()}

    text = json.dumps(rates)

    sand_smtp_email(subject, text)


def check_rate_price(rate: dict):
    preferred = info_notification["preferred"]
    msg = ""

    for ext in preferred.keys():
        if rate[ext] <= preferred[ext]:
            msg = f"{ext} reached min: {rate[ext]}"
        elif rate[ext] >= preferred[ext]:
            msg = f"{ext} reached max: {rate[ext]}"

    return msg


def send_notification(msg: str):
    pass


if __name__ == "__main__":
    res = get_rates()
    receive_time = now_time()

    if rules["archive"]:
        archive(receive_time, res["rates"])

    if rules["send_mail"]:
        send_mail(receive_time, res["rates"])

    # if rules["send_notification"]:
    #     notification_msg = check_rate_price(res["rates"])
    #     if notification_msg:
    #         send_notification(notification_msg)
