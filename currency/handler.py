import requests
import json


def get_rates(url):
    """
    send a get requests to the api.exchangerate.host api and get live rates
    :return:
    """
    try:
        response = requests.get(url)
    except requests.exceptions.ConnectionError as e:
        print(f"ERROR: The connection attempt failed.\n"
              f"Please make sure you are connected to the internet.")
        return None
    if response.status_code == 200:
        return json.loads(response.text)

    print(f"error\nYour request has encountered status code"
          f" {response.status_code}. Please check")
    return None
