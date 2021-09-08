from parsel import Selector
import requests
import time


# Requisito 1
def fetch(url):
    """Seu código deve vir aqui"""
    try:
        response = requests.get(url, timeout=3)
        time.sleep(1)
    except requests.ReadTimeout:
        return None
    if response.status_code == 200:
        return response.text
    return None


# Requisito 2

def __get_shares_count(selector):
    try:
        return int(
            selector.css('.tec--toolbar__item::text').get()
            .replace("Compartilharam", "").strip())
    except (TypeError, AttributeError):
        return 0


def __get_comments_data_count(selector):
    try:
        return int(
            selector.css('#js-comments-btn::attr(data-count)').get())
    except (TypeError, AttributeError):
        return 0


def __get_article(selector):
    return ''.join(selector.css(
        '.tec--article__body > p:nth-of-type(1) *::text').getall())


def __get_author(selector):
    writer = selector.css(
        '.tec--author__info__link::text').get()
    if not writer:
        writer = selector.css(
            '.tec--timestamp__item.z--font-bold a::text').get()
    if not writer:
        writer = selector.css(
            '.tec--author__info p::text').get()
    return writer.strip() if writer else None


def scrape_noticia(html_content):
    """Given HTML content, returns an object with selected data"""
    selector = Selector(html_content)

    news_object = {
        'url': selector.css('link[rel=canonical]::attr(href)').get(),
        'title': selector.css('#js-article-title::text').get(),
        'timestamp': selector.css('#js-article-date::attr(datetime)').get(),
        'writer': __get_author(selector),
        'shares_count': __get_shares_count(selector),
        'comments_count': __get_comments_data_count(selector),
        'summary': __get_article(selector),
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
    """Seu código deve vir aqui"""
    selector = Selector(html_content)
    href = selector.css(
        '#js-main .tec--card__title__link::attr(href)'
    ).getall()
    return href[-20:]


# Requisito 4
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
