import requests
import time


# Requisito 1
def fetch(url):
    try:
        response = requests.get(url, timeout=3)
        print(response.status_code)
    except requests.Timeout:
        response = requests.get(url, timeout=3)
        print('none')
    finally:
        print(response.text)
    time.sleep(1)
