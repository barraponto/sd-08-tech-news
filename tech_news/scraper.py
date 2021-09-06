import requests
import time
from parsel import Selector
from tech_news.database import create_news


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
    writer = selector.css(".z--font-bold").css("*::text").get() or ""
    shares_count = selector.css("div.tec--toolbar__item::text").get() or "0"

    comments_count = (
        selector.css("#js-comments-btn::attr(data-count)").get() or "0"
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
        "writer": writer.strip(),
        "shares_count": int(shares_count.strip().split()[0]),
        "comments_count": int(comments_count),
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
    news = []
    url = "https://www.tecmundo.com.br/novidades"

    while len(news) < amount:
        news_list = fetch(url)
        link = scrape_novidades(news_list)
        for x in link:
            tech_news_row = fetch(x)
            news.append(scrape_noticia(tech_news_row))
            if len(news) == amount:
                create_news(news)
                return news
        url = scrape_next_page_link(news_list)
