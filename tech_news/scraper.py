import requests
from tech_news.NewsDetailsScraper import NewsDetailsScraper
from tech_news.NewsScraper import NewsScraper
from ratelimit import limits, sleep_and_retry


# Requisito 1
@sleep_and_retry
@limits(calls=1, period=1)
def fetch(url):
    """
    Given a url returns the resulting html of the request
    Source: https://github.com/tomasbasham/ratelimit
    """
    try:
        response = requests.get(url, timeout=3)
        response.raise_for_status()
    except (requests.Timeout, requests.HTTPError):
        return None

    return response.text


# Requisito 2
def scrape_noticia(html_content):
    """Return news data as dict"""
    return NewsDetailsScraper(html_content).render()


# Requisito 3
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""
    return NewsScraper(html_content).get_news_urls()


# Requisito 4
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
