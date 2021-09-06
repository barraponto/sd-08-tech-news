import requests
import time
# from parsel import Selector
from requests.exceptions import HTTPError, ReadTimeout


# Requisito 1
def fetch(url):
    try:
        time.sleep(1)
        site = requests.get(url, timeout=3)
    except requests.Timeout:
        return None
    try:
        site.raise_for_status()
    except HTTPError:
        return None
    return site.text


# Requisito 2
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""
    # selector = Selector()
    

# Requisito 3
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
