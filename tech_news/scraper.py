import requests
import time
from parsel import Selector

# Requisito 1
def fetch(url):
    time.sleep(1)

    try:
        response = requests.get(url, timeout=3)

        if response.status_code == 200:
            return response.text
        else:
            return None
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_noticia(html_content):
    selector = Selector(text=html_content)
    return {
        "url": selector.css("head link[rel=canonical]::attr(href)").get(),
        "title": selector.css(".tec--article__header__title::text").get(),
        "timestamp": selector.css("#js-article-date::attr(datetime)").get(),
        "writer": selector.css(".tec--author__info__link::text").get().strip(),
        "shares_count": int(
            selector.css(".tec--toolbar__item::text").get().split(" ")[1]
        ),
        "comments_count": int(
            selector.css("#js-comments-btn::attr(data-count)").get()
        ),
        "summary": "".join(
            selector.css(
                ".tec--article__body p:first-of-type *::text"
            ).getall()
        ),
        "sources": [
            i.strip()
            for i in selector.css("[class='tec--badge']::text").getall()
        ],
        "categories": [
            i.strip() for i in selector.css("#js-categories a::text").getall()
        ],
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
