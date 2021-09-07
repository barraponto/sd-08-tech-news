from time import sleep
import requests


# Requisito 1
def fetch(url):
    """Given an url, fetches HTML content"""
    try:
        sleep(1)
        response = requests.get(url, timeout=3)
        response.raise_for_status()
    except (requests.Timeout, requests.HTTPError):
        return None
    return response.text


# Requisito 2
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 3
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
