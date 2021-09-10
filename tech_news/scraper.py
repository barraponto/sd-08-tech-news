import requests
from parsel import Selector
import time
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    try:
        time.sleep(1)
        response = requests.get(url, timeout=3)
        response.raise_for_status()
        return response.text
    except Exception:
        return None


# Requisito 2
def scrape_noticia(html_content):

    selector = Selector(text=html_content)
    tech_news = dict(
        url=selector.css(
            "head > meta[property='og:url']::attr(content)"
        ).get(),
        title=selector.css(".tec--article__header__title::text").get(),
        timestamp=selector.css(
            ".tec--timestamp__item time::attr(datetime)"
        ).get(),
        writer=(
            selector.css(".z--font-bold").css("*::text").get().strip() or ""
            if selector.css(".z--font-bold").css("*::text").get() is not None
            else None
        ),
        shares_count=int(
            selector.css(".tec--toolbar__item::text").get().split()[0].strip()
            if selector.css(".tec--toolbar__item::text").get() is not None
            else 0
        ),
        comments_count=int(
            selector.css(".tec--toolbar__item button::attr(data-count)").get()
            if selector.css(
                ".tec--toolbar__item button::attr(data-count)"
            ).get()
            is not None
            else 0
        ),
        summary="".join(
            selector.css(
                ".tec--article__body > p:first-child *::text"
            ).getall()
        ),
        sources=[
            source.strip()
            for source in selector.css(".z--mb-16 .tec--badge::text").getall()
        ],
        categories=[
            category.strip()
            for category in selector.css(
                "#js-categories .tec--badge::text"
            ).getall()
        ],
    )

    return tech_news


# Requisito 3
def scrape_novidades(html_content):

    selector = Selector(text=html_content)
    response = selector.css(
        "h3.tec--card__title a.tec--card__title__link::attr(href)"
    ).getall()

    return response


# Requisito 4
def scrape_next_page_link(html_content):

    selector = Selector(text=html_content)
    response = selector.css(
        "div.tec--list.tec--list--lg a.tec--btn--primary::attr(href)"
    ).get()

    return response


# Requisito 5
def get_tech_news(amount):
    URL = "https://www.tecmundo.com.br/novidades"

    content_html = fetch(URL)
    data_values = []

    while len(data_values) < amount:
        for link_novidades in scrape_novidades(content_html):
            if len(data_values) < amount:
                news = fetch(link_novidades)
                data_values.append(scrape_noticia(news))

        if len(data_values) < amount:
            next_Link = scrape_next_page_link(content_html)
            content_html = fetch(next_Link)
    create_news(data_values)
    return data_values
