import requests
import time


def fetch(url):
    try:
        time.sleep(1)
        response = requests.get(url, timeout=3)
        if response.status_code == 200:
            return response.text

        return None
    except requests.exceptions.ReadTimeout:
        return None


resposne = fetch("https://httpbin.org/status/404")

print(resposne)
