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
    # https://rockcontent.com/br/blog/canonical-tag/#oque
    url = selector.css("link[rel=canonical] ::attr(href)").get()
    title = selector.css(
        "#js-article-title ::text"
    ).get()
    time = selector.css("time ::attr(datetime)").get()
    writer = selector.css(".tec--author__info__link ::text").get().strip()
    time = selector.css("time ::attr(datetime)").get()
    shares_count = int(selector.css(
        ".tec--toolbar__item ::text"
    ).get().strip().split()[0])
    comments_count = int(
        selector.css("#js-comments-btn ::attr(data-count)").get()
    )
    summary = "".join(
        selector.css(
            "div.tec--article__body > p:nth-child(1) ::text"
        ).getall())
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

    obj = {
        "url": url,
        "title": title,
        "timestamp": time,
        "writer": writer,
        "shares_count": shares_count,
        "comments_count": comments_count,
        "summary": summary,
        "sources": sources,
        "categories": categories,
    }

    return obj


# Requisito 3
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    url = selector.css(
        "div.tec--list__item > article > div > h3 > a::attr(href)"
    ).getall()

    return url


# Requisito 4
def scrape_next_page_link(html_content):
    s = Selector(text=html_content)
    url = s.css(
        ".tec--list > a::attr(href)"
    ).get()

    return url


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
