import requests
import time


# Requisito 1
def fetch(url):
    try:
        response = requests.get("https://www.tecmundo.com.br/novidades")
        time.sleep(1)
    except requests.ReadTimeout:
        return None
    if (response.ok):
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
