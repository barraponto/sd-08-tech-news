import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    try:
        response = requests.get(url, timeout=3)
        print(response)
        time.sleep(1)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_noticia(html_content):
    selector = Selector(text=html_content)
    link = selector.css("link[rel=canonical]::attr(href)").get()
    title = selector.css(".tec--article__header__title::text").get()
    author = selector.css(".tec--author__info__link::text").get().strip()
    timestamp = selector.css("time::attr(datetime)").get()
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
    sources = [
        source.strip()
        for source in selector.css(
            "div .z--mb-16 > div > a"
        ).xpath("text()").getall()
    ]
    categories = [
        category.strip()
        for category in selector.css(
            "#js-categories > a"
        ).xpath("text()").getall()
    ]
    print(timestamp)

    result = {
        "url": link,
        "title": title,
        "timestamp": timestamp,
        "writer": author,
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
    result = selector.css(
        ".tec--list .tec--card__thumb__link::attr(href)"
        ).getall()
    return result


# Requisito 4
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    result = selector.css(
        ".tec--list > a::attr(href)"
    ).get()
    return result


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
