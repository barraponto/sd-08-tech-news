from time import sleep
import requests
from parsel import Selector


# Requisito 1
def fetch(url):
    """Seu código deve vir aqui"""
    sleep(1)
    try:
        html = requests.get(url, timeout=3)
    except requests.Timeout:
        return None
    if html.status_code != 200:
        return None
    return html.text


# Requisito 2
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)

    categories_raw = selector.css("div#js-categories a::text").getall()
    sources_raw = selector.css(".z--mb-16 > div > a::text").getall()

    return {
        "url": selector.css('meta[property="og:url"]::attr("content")').get(),
        "title": selector.css(".tec--article__header__title::text").get(),
        "timestamp": selector.css(
            ".tec--timestamp__item > time::attr(datetime)"
        ).get(),
        "writer": selector.css(".tec--author__info__link::text").get().strip(),
        "shares_count": selector.css(".tec--toolbar__item::text")
        .getall()[0]
        .split(" ")[0]
        or 0,
        "comments_count": int(selector.css(
            ".tec--toolbar > div.tec--toolbar__item *::text"
        ).get().strip().split(" ")[0]) or 0,
        "summary": "".join(
            selector.css(
                ".tec--article__body > p:nth-of-type(1) *::text"
            ).getall()
        ).strip(),
        "sources": [source.strip() for source in sources_raw],
        "categories": [category.strip() for category in categories_raw],
    }


# Requisito 3
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
