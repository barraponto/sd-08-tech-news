import requests
import time
from parsel import Selector


def fetch(url):
    try:
        time.sleep(1)
        response = requests.get(url, timeout=3)
        if response.status_code == 200:
            return response.text

        return None
    except requests.exceptions.ReadTimeout:
        return None


resposne = fetch("https://www.tecmundo.com.br/novidades")


def scrape_novidades(html_content):
    selector = Selector(text=html_content)

    return selector.css("h3.tec--card__title a::attr(href)").getall()


print(scrape_novidades(resposne))
