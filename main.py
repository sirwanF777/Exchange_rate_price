import json
import os
from datetime import datetime
from khayyam import JalaliDatetime

from config import *
from mailgun import send_mail
from notification import send_sms
from currency import get_rates


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
    res = get_rates(url_free)

    if res:
        if rules["archive"]:
            archive(res["rates"])

        if rules["mail"]["enable"]:
            send_mail(res["rates"])

        if rules["notification"]["enable"]:
            notification_msg = check_rate_price(res["rates"])
            if notification_msg:
                send_sms(notification_msg)
