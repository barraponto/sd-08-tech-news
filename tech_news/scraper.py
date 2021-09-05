import time
from parsel import Selector
from requests import get

SUCCESS = 200


# Requisito 1
def fetch(url):
    """Seu código deve vir aqui"""
    time.sleep(1)
    try:
        response = get(url, headers={"Accept": "text/html"}, timeout=3)
        return response.text if response.status_code == SUCCESS else None
    except Exception:
        return None


# Requisito 2
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    writer = selector.css("a.tec--author__info__link::text").get().strip()
    shares_count = int(
        selector.css("div.tec--toolbar__item::text")
        .get()
        .strip()
        .split(" ")[0]
    )
    comments_count = int(
        selector.css("#js-comments-btn::attr(data-count)").get()
    )
    summary = "".join(
        selector.css("div.tec--article__body > p:first-child")
        .css("*::text")
        .getall()
    )
    all_badges = [
        badge.strip() for badge in selector.css("a.tec--badge::text").getall()
    ]
    number_of_categories = len(selector.css("a.tec--badge--primary"))
    number_of_sources = len(all_badges) - number_of_categories

    return {
        "url": selector.css("link[rel=canonical]::attr(href)").get(),
        "title": selector.css("h1.tec--article__header__title::text").get(),
        "timestamp": selector.css("time::attr(datetime)").get(),
        "writer": writer,
        "shares_count": shares_count,
        "comments_count": comments_count,
        "summary": summary,
        "sources": all_badges[:number_of_sources],
        "categories": all_badges[number_of_sources:],
    }


# Requisito 3
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""
    try:
        selector = Selector(text=html_content)
        news_list = selector.css(
            ".tec--list__item .tec--card__title__link::attr(href)"
        ).getall()
        return news_list
    except Exception:
        return []


# Requisito 4
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
