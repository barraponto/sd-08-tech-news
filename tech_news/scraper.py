import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    """Returns an url content with a rate limit of 1 request per second
    and timeout of 3 seconds for each
    """
    try:
        time.sleep(1)
        response = requests.get(url, timeout=3)
        if response.status_code != 200:
            return None
        # print(response.text)
        return response.text
    except requests.exceptions.Timeout:
        return None


# Requisito 2
def scrape_noticia(html_content):
    """Returns a dict with the selected info from a html content"""
    selector = Selector(text=html_content)
    return {
        "url": selector.css('link[rel="canonical"]::attr(href)').get(),
        "title": selector.css("h1#js-article-title::text").get(),
        "timestamp": (
            selector.css(".tec--timestamp__item")
            .xpath("./time/@datetime")
            .get()
        ),
        "writer": selector.css(".tec--author__info__link::text").get().strip(),
        "shares_count": int(
            selector.css(".tec--toolbar__item::text")
            .get()
            .strip()
            .split(" ")[0]
        ),
        "comments_count": int(
            selector.css("button#js-comments-btn::attr(data-count)").get()
        ),
        "summary": selector.css(".tec--article__body")
        .xpath("string(./p)")
        .get(),
        "sources": [
            source.strip()
            for source in selector.xpath('//h2[text() = "Fontes"]/..')
            .css(".tec--badge ::text")
            .getall()
        ],
        "categories": [
            category.strip()
            for category in selector.css(
                "div#js-categories > a::text"
            ).getall()
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
