import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    try:
        response = requests.get("https://www.tecmundo.com.br/novidades")
        time.sleep(1)
    except requests.ReadTimeout:
        return None
    if (response.ok):
        return response.text


# Requisito 2
def scrape_noticia(html_content):
    selector = Selector(text=html_content)
    writer = selector.css(".tec--author__info__link::text").get()
    shares = selector.css(".tec--toolbar__item::text").re_first(r"\d+")
    comments = selector.css("#js-comments-btn ::attr(data-count)").get()
    summary = selector.css(
        "div.tec--article__body > p:nth-child(1) *::text"
    ).getall()
    sources = []
    sourcesList = selector.css(".z--mb-16 .tec--badge::text").getall()
    for source in sourcesList:
        sources.append(source.strip())
    categories = []
    categoriesList = selector.css("#js-categories > a *::text").getall()
    for categorie in categoriesList:
        categories.append(categorie.strip())

    return {
        "url": selector.css("head link[rel=canonical]::attr(href)").get(),
        "title": selector.css("#js-article-title::text").get(),
        "timestamp": selector.css("#js-article-date::attr(datetime)").get(),
        "writer": writer.strip() if writer else writer,
        "shares_count": int(shares) if shares else 0,
        "comments_count": int(comments) if comments else 0,
        "summary": "".join(summary),
        "sources": sources,
        "categories": categories,
    }


# Requisito 3
def scrape_novidades(html_content):
    selector = Selector(html_content)
    try:
        return selector.css(
            ".tec--list__item article div h3 a::attr(href)"
            ).getall()
    except Exception:
        return list()


# Requisito 4
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
