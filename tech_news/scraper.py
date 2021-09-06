import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    time.sleep(1)
    try:
        response = requests.get(url, timeout=3)
        response.raise_for_status()
        return response.text
    except Exception:
        return None


# Requisito 2
def scrape_noticia(html_content):
    selector = Selector(text=html_content)
    url_path = selector.css("link[rel=canonical]::attr(href)").get()
    page_title = selector.css("h1.tec--article__header__title::text").get()
    date_time = selector.css(
        "div.tec--timestamp__item time::attr(datetime)"
    ).get()
    writer = selector.css("a.tec--author__info__link::text").get()
    if writer:
        writer = writer.strip()
    else:
        return None
    share_count = selector.css(
        "div.tec--toolbar__item button::attr(data-count)"
    ).get()
    if share_count:
        share_count
    else:
        share_count = 0
    comments_count = selector.css(
        "div.tec--toolbar__item button::attr(data-count)"
    ).get()
    get_summary = selector.css(
        ".tec--article__body p:first-child *::text"
    ).getall()
    summary = "".join(get_summary)
    source = selector.css(".z--mb-16 .tec--badge::text").getall()
    sources = [row.strip() for row in source]
    category = selector.css("div#js-categories a::text").getall()
    categories = [row.strip() for row in category]
    return {
        "url": url_path,
        "title": page_title,
        "timestamp": date_time,
        "writer": writer,
        "shares_count": int(share_count),
        "comments_count": int(comments_count),
        "summary": summary,
        "sources": sources,
        "categories": categories,
    }


# Requisito 3
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    get_novidades = selector.css(
        ".tec--list__item .tec--card__title__link::attr(href)"
    ).getall()
    if len(get_novidades) == 0:
        return []
    else:
        return get_novidades


# Requisito 4
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    next_page = selector.css(".tec--btn ::attr(href)").get()
    return next_page or None


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
