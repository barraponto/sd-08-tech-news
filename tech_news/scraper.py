import requests
import time
from parsel import Selector
from tech_news.database import create_news


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
    tech_news = {}
    selector = Selector(text=html_content)
    tech_news["url"] = selector.css(
        "head > meta[property='og:url']::attr(content)"
    ).get()
    tech_news["title"] = selector.css(
        ".tec--article__header__title::text"
    ).get()
    tech_news["timestamp"] = selector.css(
        ".tec--timestamp__item time::attr(datetime)"
    ).get()
    tech_news["writer"] = (
        selector.css(".z--font-bold").css("*::text").get().strip() or ""
        if selector.css(".z--font-bold").css("*::text").get() is not None
        else None
    )
    tech_news["shares_count"] = int(
        selector.css(".tec--toolbar__item::text").get().split()[0].strip()
        if selector.css(".tec--toolbar__item::text").get() is not None
        else 0
    )
    tech_news["comments_count"] = int(
        selector.css(".tec--toolbar__item button::attr(data-count)").get()
        if selector.css(".tec--toolbar__item button::attr(data-count)").get()
        is not None
        else 0
    )
    tech_news["summary"] = "".join(
        selector.css(".tec--article__body > p:first-child *::text").getall()
    )
    tech_news["sources"] = [
        source.strip()
        for source in selector.css(".z--mb-16 .tec--badge::text").getall()
    ]
    tech_news["categories"] = [
        category.strip()
        for category in selector.css(
            "#js-categories .tec--badge::text"
        ).getall()
    ]
    return tech_news


# Requisito 3
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    return selector.css(
        "h3.tec--card__title a.tec--card__title__link::attr(href)"
    ).getall()


# Requisito 4
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    return selector.css(
        "div.tec--list.tec--list--lg a.tec--btn--primary::attr(href)"
    ).get()


# Requisito 5
def get_tech_news(amount):
    tech_news = []
    tech_news_url = "https://www.tecmundo.com.br/novidades"

    while len(tech_news) < amount:
        tech_news_list = fetch(tech_news_url)
        tech_news_link = scrape_novidades(tech_news_list)
        for row in tech_news_link:
            tech_news_row = fetch(row)
            tech_news.append(scrape_noticia(tech_news_row))
            if len(tech_news) == amount:
                create_news(tech_news)
                return tech_news
        tech_news_url = scrape_next_page_link(tech_news_list)
