from time import sleep
import requests
from requests.exceptions import Timeout
from parsel import Selector
from tech_news.database import create_news


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
# Refatoração desenvolvida com o apoio do amigo Hugo Braga
def scrape_writer(selector):
    writer = None
    first_writer_type = selector.css(
        ".tec--author__info__link").xpath("text()").get()

    second_writer_type = selector.css(
        "a[href*=autor]").xpath("text()").get()

    third_writer_type = selector.css(
        ".tec--author__info> p::text").get()

    if first_writer_type:
        writer = first_writer_type.strip()
    elif second_writer_type:
        writer = second_writer_type.strip()
    elif third_writer_type:
        writer = third_writer_type
    return writer


def scrape_noticia(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)

    shares_count_beta = selector.css(".tec--toolbar__item::text").get()
    if shares_count_beta:
        shares_count = int(shares_count_beta.strip().split(" ")[0])
    else:
        shares_count = 0

    return {
        "url": selector.css("link[rel=canonical]::attr(href)").get(),

        "title": selector.css("#js-article-title::text").get(),

        "timestamp": selector.css("#js-article-date::attr(datetime)").get(),

        "writer": scrape_writer(selector),

        "shares_count": shares_count,

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
    news = []
    url = "https://www.tecmundo.com.br/novidades"

    while len(news) < amount:
        news_list = fetch(url)
        links = scrape_novidades(news_list)
        for link in links[:amount - len(news)]:
            news_item = fetch(link)
            news.append(scrape_noticia(news_item))
        url = scrape_next_page_link(news_list)
    create_news(news)
    return news
