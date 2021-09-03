import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    """Seu código deve vir aqui"""
    time.sleep(1)
    try:
        response = requests.get(url, timeout=3)
        if response.status_code != 200:
            return None
        return response.text
    except requests.Timeout:
        return None


# Requisito 2
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    sources = selector.css("a[target].tec--badge *::text").getall()
    categories = selector.css("#js-categories a *::text").getall()
    summary = ''.join(selector.css(
          "div .tec--article__body p:first-of-type *::text").getall())
    object = {
        "url": selector.css("link[rel^=canonical]::attr(href)").get(),
        "title": selector.css(".tec--article__header__title *::text").get(),
        "timestamp": selector.css("#js-article-date::attr(datetime)").get(),
        "writer": selector
        .css(".tec--author__info__link *::text").get().strip(),
        "shares_count": int(selector.css(
          "div .tec--toolbar__item *::text").get().split()[0]) or 0,
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
    """Seu código deve vir aqui"""
