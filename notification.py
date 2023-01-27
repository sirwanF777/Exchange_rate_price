from kavenegar import *

from config import info_notification as notification


def send_sms(msg):
    try:
        api = KavenegarAPI(notification["API_key"])
        params = {
            'sender': "",
            # multiple mobile number, split by comma
            'receptor': notification["receiver"],
            'message': msg,
        }
        response = api.sms_send(params)
        print(f"{response}\nSMS sent successfully.")
    except APIException as e:
        print(e)
    except HTTPException as e:
        print(e)
