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
    except (requests.Timeout, requests.HTTPError):
        return None
    return response.text


# Requisito 2
def scrape_noticia(html_content):
    """Given HTML content, returns an object with selected data"""
    selector = Selector(html_content)

    def get_writer():
        writer = selector.css(
            '.tec--author__info__link::text').get()
        if not writer:
            writer = selector.css(
                '.tec--timestamp__item.z--font-bold a::text').get()
        if not writer:
            writer = selector.css(
                '.tec--author__info p::text').get()
        return writer.strip() if writer else None

    def get_shares_count():
        try:
            return int(
                selector.css('.tec--toolbar__item::text').get()
                .replace("Compartilharam", "").strip())
        except AttributeError:
            return 0

    news_object = {
        'url': selector.css('link[rel=canonical]::attr(href)').get(),
        'title': selector.css('#js-article-title::text').get(),
        'timestamp': selector.css('#js-article-date::attr(datetime)').get(),
        'writer': get_writer(),
        'shares_count': get_shares_count(),
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

    url_list = selector.css(
        '#js-main .tec--card__title__link::attr(href)'
    ).getall()
    return url_list


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
    """Seu código deve vir aqui"""
    tech_news = []
    tech_news_url = "https://www.tecmundo.com.br/novidades"

    while len(tech_news) < amount:
        tech_news_list = fetch(tech_news_url)
        tech_news_link = scrape_novidades(tech_news_list)
        for row in tech_news_link:
            tech_news_row = fetch(row)
            tech_news.append(scrape_noticia(tech_news_row))
            if len(tech_news) == amount:
                create_news(tech_news)
                return tech_news
        tech_news_url = scrape_next_page_link(tech_news_list)
