import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    """Seu código deve vir aqui"""
    try:
        time.sleep(1)
        response = requests.get(url, timeout=3)
    except requests.ReadTimeout:
        return None
    if response.status_code == 200:
        return response.text
    else:
        return None


def get_writer(html_content):
    selector = Selector(text=html_content)

    try:
        writer = selector.css(".tec--author__info__link::text").get()
        return writer.strip()
    except AttributeError:
        return None


def get_shares_count(html_content):
    selector = Selector(html_content)
    try:
        shares_count = selector.css(".tec--toolbar__item::text").get()
        return int(shares_count.strip().split(" ")[0])
    except (TypeError, AttributeError):
        return 0


def get_comments_count(html_content):
    selector = Selector(html_content)
    try:
        comments_count = selector.css(
            "#js-comments-btn::attr(data-count)"
        ).get()
        return int(comments_count)
    except (TypeError, AttributeError):
        return 0


def get_summary(html_content):
    selector = Selector(html_content)
    try:
        summary = selector.css(
            ".tec--article__body p:first-child *::text"
        ).getall()
        return "".join(summary)
    except (TypeError, AttributeError):
        return None


def get_sources(html_content):
    selector = Selector(html_content)
    try:
        sources = []
        sourcesList = selector.css(".z--mb-16 .tec--badge::text").getall()
        for source in sourcesList:
            sources.append(source.strip())
        return sources
    except (TypeError, AttributeError):
        return None


def get_categories(html_content):
    selector = Selector(html_content)
    try:
        categories = []
        categoriesList = selector.css("#js-categories > a *::text").getall()
        for categorie in categoriesList:
            categories.append(categorie.strip())
        return categories
    except (TypeError, AttributeError):
        return None


# Requisito 2
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)

    return {
        "url": selector.css("head link[rel=canonical]::attr(href)").get(),
        "title": selector.css("#js-article-title::text").get(),
        "timestamp": selector.css("#js-article-date::attr(datetime)").get(),
        "writer": get_writer(html_content),
        "shares_count": get_shares_count(html_content),
        "comments_count": get_comments_count(html_content),
        "summary": get_summary(html_content),
        "sources": get_sources(html_content),
        "categories": get_categories(html_content),
    }


# Requisito 3
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    selector_links = selector.css(
        ".tec--list__item  .tec--card__title__link::attr(href)"
    ).getall()
    return selector_links


# Requisito 4
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
