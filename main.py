import requests
import json
import os
from datetime import datetime
from khayyam import JalaliDatetime

from config import *
from mailgun import send_mail
from notification import send_sms


def get_rates():
    """
    send a get requests to the api.exchangerate.host api and get live rates
    :return:
    """
    try:
        response = requests.get(url_free)
    except requests.exceptions.ConnectionError as e:
        print(f"ERROR: The connection attempt failed.\n"
              f"Please make sure you are connected to the internet.")
        return None
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


def check_rate_price(rate):
    """
    check if user defined notify rules and if rate reached to the defined
    rules, then generate proper msg to send.
    :param rate:
    :return:mag(str)
    """
    preferred = rules["notification"]["preferred"]
    msg = ""

    for ext in preferred.keys():
        if rate[ext] <= preferred[ext]["min"]:
            msg = str(JalaliDatetime.now().strftime('%C'))
            msg += f"\n{ext} reached min: {rate[ext]}\n"
        elif rate[ext] >= preferred[ext]["max"]:
            msg = str(JalaliDatetime.now().strftime('%C'))
            msg += f"\n{ext} reached max: {rate[ext]}\n"

    return msg


if __name__ == "__main__":
    res = get_rates()

    if res:
        if rules["archive"]:
            archive(res["rates"])

        if rules["mail"]["enable"]:
            send_mail(res["rates"])

        if rules["notification"]["enable"]:
            notification_msg = check_rate_price(res["rates"])
            if notification_msg:
                send_sms(notification_msg)
