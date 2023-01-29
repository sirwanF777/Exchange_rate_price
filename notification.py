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
        print(f"ERROR: {str(e)[2:19]}\n"
              f"Please, according to the error that occurred,"
              f"Follow the cause of your error through the website address below.\n"
              f"https://kavenegar.com/soap.html")
    except HTTPException as e:
        print(e)
