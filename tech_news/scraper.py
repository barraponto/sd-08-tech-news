from time import sleep
import requests
from requests.exceptions import Timeout
from parsel import Selector


# Requisito 1
def fetch(url):
    """Seu código deve vir aqui"""
    try:
        response = requests.get(url, timeout=3)
        if response.status_code == 200:
            return response.text
    except Timeout:
        return None

    sleep(1)


# Requisito 2
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 3
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    return selector.css(
        ".tec--list__item  .tec--card__title__link::attr(href)"
    ).getall()


# Requisito 4
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    return selector.css(
        ".tec--btn--primary::attr(href)"
    ).get()


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
