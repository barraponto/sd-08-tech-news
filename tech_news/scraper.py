import requests
import time
from parsel import Selector
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    time.sleep(1)

    try:
        response = requests.get(url, timeout=3)

        if response.status_code == 200:
            return response.text
        else:
            return None
    except requests.ReadTimeout:
        return None


# Requisito 2
def set_author(selector):
    writer = selector.css(".tec--author__info__link::text").get()

    if writer is None:
        writer = selector.css(
            ".tec--article__body-grid div div div div a::text"
        ).get()
        if writer is None:
            return None
        else:
            if writer == " ":
                return "Equipe TecMundo"
            else:
                return writer.strip()
    else:
        return writer.strip()


def set_comments(comments):
    if comments is None:
        return 0
    else:
        return int(comments)


def scrape_noticia(html_content):
    selector = Selector(text=html_content)
    shares_count = selector.css(".tec--toolbar__item::text").get()
    if shares_count is None:
        result = 0
    else:
        shares_count = selector.css(".tec--toolbar__item::text").getall()
        shares_count = int(shares_count[0].split()[0])
        result = shares_count

    return {
        "url": selector.css("head link[rel=canonical]::attr(href)").get(),
        "title": selector.css(".tec--article__header__title::text").get(),
        "timestamp": selector.css("#js-article-date::attr(datetime)").get(),
        "writer": set_author(selector),
        "shares_count": int(result),
        "comments_count": set_comments(
            selector.css("#js-comments-btn::attr(data-count)").get()
        ),
        "summary": "".join(
            selector.css(
                ".tec--article__body > p:first-of-type *::text"
            ).getall()
        ),
        "sources": [
            i.strip()
            for i in selector.css("[class='tec--badge']::text").getall()
        ],
        "categories": [
            i.strip() for i in selector.css("#js-categories a::text").getall()
        ],
    }


# Requisito 3
def scrape_novidades(html_content):
    selector = Selector(text=html_content)

    url = selector.css(
        "div.tec--list__item > article > div > h3 > a::attr(href)"
    ).getall()

    return url


# Requisito 4
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)

    url = selector.css(
        ".tec--list > a::attr(href)"
    ).get()

    return url


# Requisito 5
def get_tech_news(amount):
    news_list = fetch("https://www.tecmundo.com.br/novidades")
    news = []

    while len(news) < amount:
        for link in scrape_novidades(news_list):
            if len(news) < amount:
                act_news = fetch(link)
                news.append(scrape_noticia(act_news))

        if len(news) < amount:
            next_link = scrape_next_page_link(news_list)
            news_list = fetch(next_link)
    create_news(news)
    return news