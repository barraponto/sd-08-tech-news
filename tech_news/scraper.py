import requests
import time
import math
from tech_news.database import create_news
from parsel import Selector

from requests.exceptions import ReadTimeout


# Requisito 1
def fetch(url):
    try:
        request = requests.get(url, timeout=3)
        time.sleep(1)
        if(request.status_code == 200):
            return request.text
        else:
            return None
    except ReadTimeout:
        return None


# Requisito 2
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    sources = selector.css("a[target].tec--badge *::text").getall()
    categories = selector.css("#js-categories a *::text").getall()
    summary = ''.join(selector.css(
        ".tec--article__body > p:first-child *::text").getall())
    writer = selector.css(".tec--author__info__link *::text").get()
    shares_count = selector.css(
        "div .tec--toolbar__item *::text").get().split()
    object = {
        "url": selector.css("link[rel^=canonical]::attr(href)").get(),
        "title": selector.css(".tec--article__header__title *::text").get(),
        "timestamp": selector.css("#js-article-date::attr(datetime)").get(),
        "writer": writer.strip() if writer is not None else None,
        "shares_count": int(shares_count[0]) if len(shares_count) != 0 else 0,
        "comments_count": int(selector.css(
          "#js-comments-btn::attr(data-count)").get()),
        "summary": summary.replace('."', '. "'),
        "sources": list(map(str.strip, sources)),
        "categories": list(map(str.strip, categories)),
    }

    return object


# Requisito 3
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""
    try:
        selector = Selector(text=html_content)
        return selector.css("h3 a.tec--card__title__link::attr(href)").getall()
    except ValueError:
        return []


# Requisito 4
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    try:
        selector = Selector(text=html_content)
        return selector.css(
            "a:last-child.tec--btn::attr(href)").get()
    except ValueError:
        return []


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui """
    url = "https://www.tecmundo.com.br/novidades"
    url_list = []
    data_list = []
    pages_number = math.ceil(amount / 20)
    for index in range(pages_number):
        page = scrape_novidades(fetch(url))
        url = scrape_next_page_link(fetch(url))
        for index in page:
            url_list.append(index)
    for index in range(amount):
        data_list.append(scrape_noticia(fetch(url_list[index])))
    print(len(url_list))
    create_news(data_list)
    return data_list
