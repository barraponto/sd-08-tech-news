from parsel import Selector
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
    """Given HTML content, returns an object with selected data"""
    selector = Selector(html_content)

    news_object = {
        'url': selector.css('link[rel=canonical]::attr(href)').get(),
        'title': selector.css('#js-article-title::text').get(),
        'timestamp': selector.css('#js-article-date::attr(datetime)').get(),
        'writer': selector.css('.tec--author__info__link::text').get().strip(),
        'shares_count': int(
            selector.css('.tec--toolbar__item::text').get()
            .replace("Compartilharam", "").strip()),
        'comments_count': int(
            selector.css('#js-comments-btn::attr(data-count)').get()),
        'summary': ''.join(selector.css(
            '.tec--article__body p:first-child *::text'
            ).getall()),
        'sources': [source.strip() for source in selector.css(
            '.z--mb-16 .tec--badge::text'
            ).getall()],
        'categories': [category.strip() for category in selector.css(
            '#js-categories a::text'
            ).getall()],
    }

    return news_object


# Requisito 3
def scrape_novidades(html_content):
    """Returns a list with URLs"""
    selector = Selector(html_content)

    link_list = selector.css('.tec--card__thumb__link::attr(href)').getall()
    return link_list


# Requisito 4
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
