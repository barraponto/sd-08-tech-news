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
    writer = selector.css(".tec--author__info__link ::text").get()
    time = selector.css("time ::attr(datetime)").get()
    shares_count = selector.css(".tec--toolbar__item ::text").get()
    comments_count = selector.css("#js-comments-btn ::attr(data-count)").get()
    summary = selector.css(
        "div.tec--article__body z--px-16 p402_premium > p:nth-child(1) *::text"
    ).getall()
    print(url, title, writer, time, shares_count, comments_count, summary)


# Requisito 3
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
