import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    time.sleep(1)

    try:
        response = requests.get(url, timeout=3)
    except requests.ReadTimeout:
        return None
    if response.ok:
        return response.text


# Requisito 2
def scrape_noticia(html_content):
    selector = Selector(text=html_content)
    url = selector.css("link[rel=canonical]::attr(href)").get()
    title = selector.css(".tec--article__header__title::text").get()
    timestamp = selector.css("time::attr(datetime)").get()
    writer = selector.css(".tec--author__info__link::text").get().strip()
    shares_count = int(
        selector.css(".tec--toolbar__item::text").get().strip().split()[0]
    )
    comments_count = int(
        selector.css("#js-comments-btn ::attr(data-count)").get()
    )
    summary = "".join(
        selector.css(
            "div .tec--article__body > p:nth-child(1) ::text"
        ).getall()
    )
    sources = []
    sources_list = selector.css(".z--mb-16 .tec--badge::text").getall()
    for source in sources_list:
        sources.append(source.strip())

    categories = []
    categories_list = selector.css("#js-categories > a *::text").getall()
    for category in categories_list:
        categories.append(category.strip())

    result = {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "shares_count": shares_count,
        "comments_count": comments_count,
        "summary": summary,
        "sources": sources,
        "categories": categories,
    }
    return result


# Requisito 3
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    return selector.css(
            ".tec--list__item > article > div > h3 > a::attr(href)"
    ).getall()


# Requisito 4
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
