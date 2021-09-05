from parsel import Selector
import time
import requests
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    try:
        time.sleep(1)
        response = requests.get(url, timeout=3)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except requests.ReadTimeout:
        return None

# https://algoritmosempython.com.br/cursos/programacao-python/strings/


# Requisito 2
def get_writer(selector):
    writer = selector.css(
        "#js-author-bar > div >p.z--m-none.z--truncate.z--font-bold > a::text"
    ).get()
    if not writer:
        return None
    return writer.strip()


def get_shares_count(selector):
    shares_count = selector.css(
        "#js-author-bar > nav > div:nth-child(1)::text"
        ).get()
    shares_count = shares_count[0]
    if shares_count == " ":
        shares_count = 0
    return shares_count


def get_comments_count(selector):
    comments_count = selector.css("#js-comments-btn::text").get()
    if comments_count == " ":
        comments_count = 0
    return comments_count


# https://www.delftstack.com/pt/howto/python/how-to-remove-whitespace-in-a-string
def get_summary(selector):
    summary = ' '
    summary_itens = selector.css(
            "div.tec--article__body > p:nth-child(1) *::text"
        ).getall()
    for item in summary_itens:
        summary += item
    return summary.lstrip()


def get_sources(selector):
    sources_items = selector.css(
        "#js-main > div.z--container > article >"
        "div.tec--article__body-grid > div.z--mb-16.z--px-16 > div > a::text"
    ).getall()
    sources = []
    for item in sources_items:
        sources.append(item.strip())
    return sources


def get_categories(selector):
    categories_items = selector.css("#js-categories a::text").getall()
    categories = []
    for item in categories_items:
        categories.append(item.strip())
    return categories


def scrape_noticia(html_content):
    news = {}
    selector = Selector(text=html_content)
    news["url"] = selector.css("head > link[rel=canonical]::attr(href)").get()
    news["title"] = selector.css("#js-article-title::text").get()
    news["timestamp"] = selector.css("#js-article-date::attr(datetime)").get()
    news["writer"] = get_writer(selector)
    news["shares_count"] = get_shares_count(selector)
    news["comments_count"] = get_comments_count(selector)
    news["summary"] = get_summary(selector)
    news["sources"] = get_sources(selector)
    news["categories"] = get_categories(selector)
    return news


# Requisito 3
def scrape_novidades(html_content):
    news = []
    selector = Selector(text=html_content)
    news = selector.css(
        "div > div > article > div > h3 > a::attr(href)"
    ).getall()
    return news


# Requisito 4
def scrape_next_page_link(html_content):
    next_page_link = ' '
    selector = Selector(text=html_content)
    next_page_link = selector.css(
        "#js-main > div > div > div.z--col.z--w-2-3 >"
        "div.tec--list.tec--list--lg > a::attr(href)"
    ).get()
    if not next_page_link:
        return None
    return next_page_link


# Requisito 5
def get_tech_news(amount):
    tech_news = []
    html = fetch("https://www.tecmundo.com.br/novidades")
    next = scrape_next_page_link(html)
    while amount:
        tech_news.append(scrape_noticia(html))
        if next is not None:
            tech_news.append(scrape_next_page_link(html))
            amount -= len(tech_news)
    create_news(tech_news)
    return tech_news
