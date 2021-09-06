import requests
import time
from parsel import Selector
from tech_news.database import create_news


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
def get_writer(selector):
    writer = selector.css(".tec--author__info__link::text").get()
    if not writer:
        writer = selector.css(
            ".tec--timestamp.tec--timestamp--lg a::text"
        ).get()
    if not writer:
        writer = selector.css(".tec--author__info p::text").get()
    return writer.strip() if writer else None


def scrape_noticia(html_content):
    selector = Selector(text=html_content)
    url = selector.css("link[rel=canonical]::attr(href)").get()
    title = selector.css(".tec--article__header__title::text").get()
    timestamp = selector.css("time::attr(datetime)").get()
    writer = get_writer(selector)
    shares_count = selector.css(".tec--toolbar__item::text").get()
    if (type(shares_count) == str):
        shares_count = int(shares_count.strip().split()[0])
    else:
        shares_count = 0
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
    selector = Selector(text=html_content)
    return selector.css(
        ".tec--list > a::attr(href)"
    ).get()


# Requisito 5
def get_tech_news(amount):
    URL = "https://www.tecmundo.com.br/novidades"

    html_contents = fetch(URL)
    data = []

    while len(data) < amount:
        for link in scrape_novidades(html_contents):
            if len(data) < amount:
                html_news = fetch(link)
                data.append(scrape_noticia(html_news))

        if len(data) < amount:
            next_link = scrape_next_page_link(html_contents)
            html_contents = fetch(next_link)
    create_news(data)
    return data
