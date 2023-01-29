from kavenegar import *


def send_sms(API_key, msg, receiver):
    try:
        api = KavenegarAPI(API_key)
        params = {
            'sender': "",
            # multiple mobile number, split by comma
            'receptor': receiver,
            'message': msg,
        }
        response = api.sms_send(params)
        print(f"{response}\nSMS sent successfully.")
    except APIException as e:
        print(f"ERROR: {str(e)[2:20]}\n"
              f"Please, according to the error that occurred,"
              f"Follow the cause of your error through the website address below.\n"
              f"https://kavenegar.com/soap.html")
    except HTTPException as e:
        print(e)
