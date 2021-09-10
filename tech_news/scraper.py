import requests
import time
from parsel import Selector
from tech_news.database import create_news


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


# Requisito 1
def fetch(url):
    time.sleep(1)
    try:
        request = requests.get(url, timeout=3)
        if request.status_code != 200:
            return None
        return request.text
    except (requests.Timeout, requests.HTTPError):
        return None


# Requisito 2
def scrape_noticia(html_content):
    selector = Selector(text=html_content)
    sources = selector.css('.z--mb-16 a::text').getall()
    sources = [source.strip() for source in sources]
    categories = selector.css('#js-categories a::text').getall()
    categories = [categorie.strip() for categorie in categories]
    return {
        "url": selector.css('link[rel=canonical]::attr(href)').get(),
        "title": selector.css('.tec--article__header__title ::text').get(),
        "timestamp": selector.css(
            '.tec--timestamp__item time::attr(datetime)'
        ).get(),
        "writer": get_writer(selector),
        "shares_count": get_shares_count(selector),
        "comments_count": get_comments_count(selector),
        "summary": "".join(selector.css(
            '.tec--article__body > p:nth-of-type(1) *::text'
        ).getall()),
        "sources": sources,
        "categories": categories,
    }


# Requisito 3
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    if selector:
        urls = selector.css('.tec--card__title__link ::attr(href)').getall()
        return urls[-20:]
    return []


# Requisito 4
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    return selector.css('.tec--btn ::attr(href)').get()


# Requisito 5
def get_tech_news(amount):
    url = 'https://www.tecmundo.com.br/novidades'
    news = []
    while len(news) < amount:
        page = fetch(url)
        links = scrape_novidades(page)
        for url in links:
            html = fetch(url)
            formatted_new = scrape_noticia(html)
            news.append(formatted_new)
            if (len(news) >= amount):
                break
        url = scrape_next_page_link(page)
    create_news(news)
    return news
