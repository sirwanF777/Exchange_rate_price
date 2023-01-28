# API key and website address app.currencyapi.com you can login if you want
BASE_PATH = 'https://api.currencyapi.com/v3/latest?apikey='
API_KEY = 'CnLGNapXhCBs4LZsv5yvl0PYgQMOuipVHZhvVbQq'

url_pro = BASE_PATH + API_KEY
url_free = "https://api.exchangerate.host/latest"

info_mail = {
    "smtp_server": "smtp.gmail.com",
    "port": 465,

    "sender": "sender's email: info@progillss.com",
    "password": "sender's email password",
    "receiver": "receiver's email: info@progillss.com",
    # preferred default is None,
    # preferred = None,
    "preferred": ["ANG", "BTC", "EUR", "IRR"]
}

info_notification = {
    # receiver phone number
    "receiver": "09***",
    # your api ket in kavenegar site
    "API_key": "",
    "preferred": {
        "ANG": {"min": 1.3, "max": 2.5},
        "IRR": {"min": 39000, "max": 50000}
    }
}

rules = {
    "archive": True,
    "send_mail": False,
    "send_notification": False
}
