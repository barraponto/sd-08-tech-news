import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    time.sleep(1)
    try:
        response = requests.get(url, timeout=3)
        if response.status_code != 200:
            return None
        return response.text
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_noticia(html_content):
    selector = Selector(text=html_content)
    url = selector.css("link[rel=canonical]::attr(href)").get()
    title = selector.css("#js-article-title::text").get()
    timestamp = selector.css("#js-article-date::attr(datetime)").get()
    writer = selector.css("#js-author-bar div a::text").get().strip()
    shares_count = selector.css("tec--toolbar__item :last-child::text") \
        .re_first(r"\d+", default=0)
    comments_count = selector.css("#js-comments-btn :last-child::text") \
        .re_first(r"\d+", default=0)
    summary = ''.join(selector
                      .css(".tec--article__body p:first-child *::text")
                      .getall())
    sources = selector.css("div:not(#js-categories) > a.tec--badge::text") \
                      .re(r"\S.*\S")
    categories = selector.css("#js-categories a::text").re(r"\S.*\S")
    return {"url": url, "title": title, "timestamp": timestamp,
            "writer": writer,
            "shares_count": shares_count, "comments_count": comments_count,
            "summary": summary,
            "sources": sources, "categories": categories}


# Requisito 3
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
