from ratelimit import limits, sleep_and_retry
import requests


# Requisito 1
@sleep_and_retry
@limits(calls=1, period=1)
def fetch(url):
    """
    Make an HTTP request with GET Method to the url received as param.

    Returns the HTML text if receive an response with status code is 200 within
    3 seconds, otherwise returns None.
    """
    try:
        response = requests.get(url, timeout=3)
        if response.status_code != 200:
            return None
        return response.text
    except requests.Timeout:
        return None


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
