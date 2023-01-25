# API key and website address app.currencyapi.com you can login if you want
BASE_PATH = 'https://api.currencyapi.com/v3/latest?apikey='
API_KEY = 'CnLGNapXhCBs4LZsv5yvl0PYgQMOuipVHZhvVbQq'

url_pro = BASE_PATH + API_KEY
url_free = "https://api.exchangerate.host/latest"

info_mail = {
    "smtp_server": "smtp.gmail.com",
    "port": 465,
    "sender": "sirwan.farajpanah79@gmail.com",
    "password": "juvviqgmkujefzim",
    "receiver": "sirwan.farajpanah1379@gmail.com",
    # "email_receiver": "info@progillss.com",
    # preferred default is None,
    # preferred = None,
    "preferred": ["ANG", "BTC", "EUR", "IRR"]
}

info_notification = {
    "receiver": "09109107005",
    "preferred": {
        "ANG": {"min": 1.3, "max": 2.5},
        "IRR": {"min": 39000, "max": 50000}
    }
}

rules = {
    "archive": True,
    "send_mail": True,
    "send_notification": True
}
