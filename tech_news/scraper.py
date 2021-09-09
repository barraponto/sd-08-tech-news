import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    try:
        response = requests.get(url, timeout=3)
        time.sleep(1)
        if response.status_code != 200:
            return None
        else:
            return response.text
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_noticia(html_content):
    selector = Selector(text=html_content)
    link = selector.css("link[rel=canonical]::attr(href)").get()
    title = selector.css(".tec--article__header__title::text").get()
    timestamp = selector.css("time::attr(datetime)").get()
    author = selector.css(".z--font-bold").css("*::text").get() or ""
    shares_count = (
        selector.css("div.tec--toolbar__item::text").get() or "0"
    )
    comments_count = (
        selector.css("#js-comments-btn ::attr(data-count)").get() or "0"
    )
    summary = "".join(
        selector.css(
            "div .tec--article__body > p:nth-child(1) ::text"
        ).getall()
    )
    sources = [
        source.strip() for source in selector.css(
            "div .z--mb-16 > div > a"
        ).xpath("text()").getall()
    ]
    categories = [
        category.strip() for category in selector.css(
            "#js-categories > a"
        ).xpath("text()").getall()
    ]

    result = {
        "url": link,
        "title": title,
        "timestamp": timestamp,
        "writer": author.strip(),
        "shares_count": int(shares_count.strip().split()[0]),
        "comments_count": int(comments_count),
        "summary": summary,
        "sources": sources,
        "categories": categories,
    }
    return result


# Requisito 3
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
