from parsel import Selector
from tech_news.database import create_news
from time import sleep
import requests


# Requisito 1
def fetch(url):
    """Given an url, fetches HTML content"""
    try:
        sleep(1)
        response = requests.get(url, timeout=3)
        response.raise_for_status()
        return response.text
    except (requests.Timeout, requests.HTTPError):
        return None


# Requisito 2
def get_writer(selector):
    writer = selector.css(
        '.tec--author__info__link::text').get()
    if not writer:
        writer = selector.css(
            '.tec--timestamp__item.z--font-bold a::text').get()
    if not writer:
        writer = selector.css(
            '.tec--author__info p::text').get()
    return writer.strip() if writer else None


def get_shares_count(selector):
    try:
        return int(
            selector.css('.tec--toolbar__item::text').get()
            .replace("Compartilharam", "").strip())
    except (AttributeError, TypeError):
        return 0


def get_comments_count(selector):
    try:
        return int(
            selector.css('#js-comments-btn::attr(data-count)').get())
    except (AttributeError, TypeError):
        return 0


def get_summary(selector):
    return ''.join(selector.css(
        '.tec--article__body > p:nth-of-type(1) *::text').getall())


def scrape_noticia(html_content):
    """Given HTML content, returns an object with selected data"""
    selector = Selector(html_content)

    news_object = {
        'url': selector.css('link[rel=canonical]::attr(href)').get(),
        'title': selector.css('#js-article-title::text').get(),
        'timestamp': selector.css('#js-article-date::attr(datetime)').get(),
        'writer': get_writer(selector),
        'shares_count': get_shares_count(selector),
        'comments_count': get_comments_count(selector),
        'summary': get_summary(selector),
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

    url_list = selector.css(
        '#js-main .tec--card__title__link::attr(href)'
    ).getall()
    return url_list[-20:]


# Requisito 4
def scrape_next_page_link(html_content):
    """Returns the link for the next page"""
    selector = Selector(html_content)
    next_page_link = selector.css(
        'div.tec--list.tec--list--lg a.tec--btn--primary::attr(href)'
    ).get()
    return next_page_link


# Requisito 5
def get_tech_news(amount):
    """Populate database with news data and return fetched news"""
    url = "https://www.tecmundo.com.br/novidades"
    tech_news = []
    while len(tech_news) < amount:
        current_page = fetch(url)
        url_list = scrape_novidades(current_page)
        for url in url_list:
            content = fetch(url)
            news = scrape_noticia(content)
            tech_news.append(news)
            if len(tech_news) >= amount:
                break
        url = scrape_next_page_link(current_page)
    create_news(tech_news)
    return tech_news
