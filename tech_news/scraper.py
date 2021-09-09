from time import sleep
import requests
from requests.exceptions import Timeout
from parsel import Selector


# Requisito 1
def fetch(url):
    """Seu código deve vir aqui"""
    try:
        response = requests.get(url, timeout=3)
        if response.status_code == 200:
            return response.text
    except Timeout:
        return None

    sleep(1)


# Requisito 2
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)

    return {
        "url": selector.css("link[rel=canonical]::attr(href)").get(),

        "title": selector.css("#js-article-title::text").get(),

        "timestamp": selector.css("#js-article-date::attr(datetime)").get(),

        "writer": selector.css(".tec--author__info__link::text").get().strip(),

        "shares_count": int(
            selector.css(".tec--toolbar__item::text")
            .get()
            .strip()
            .split(" ")[0]),

        "comments_count": int(
            selector.css("#js-comments-btn::attr(data-count)").get()),

        "summary": "".join(
            selector.css(
                ".tec--article__body > p:first-child *::text"
            ).getall()),

        "sources": [
            source.strip() for source in selector.css(
                ".z--mb-16 .tec--badge::text"
            ).getall()],

        "categories": [
            category.strip() for category in selector.css(
                "#js-categories > a *::text"
            ).getall()],
    }


# Requisito 3
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    return selector.css(
        ".tec--list__item  .tec--card__title__link::attr(href)"
    ).getall()


# Requisito 4
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    return selector.css(
        ".tec--btn--primary::attr(href)"
    ).get()


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
