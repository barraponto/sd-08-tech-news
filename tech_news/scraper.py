import requests
import time
from parsel import Selector

from tech_news.GetScrapeNoticia import GetScrapeNoticia


# Requisito 1
def fetch(url):
    """Seu código deve vir aqui"""
    try:
        response = requests.get(url, timeout=3)
        time.sleep(1)
        if response.status_code != 200:
            return None
        return response.text
    except requests.Timeout:
        return None


# Requisito 2
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""
    return GetScrapeNoticia(html_content).news_dictionary()


# Requisito 3
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(html_content)
    return selector.css(
        ".tec--list .tec--card .tec--card__thumb__link::attr(href)"
    ).getall()


# Requisito 4
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(html_content)
    return selector.css(".tec--list .tec--btn::attr(href)").get()


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
