import requests
import time

from parsel import Selector
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    time.sleep(1)
    try:
        response = requests.get(url, timeout=3)
        status = response.status_code
        if status != 200:
            return None
        return response.text
    except requests.Timeout:
        return None


def make_url(selector):
    str_url = "head link[rel=canonical]::attr(href)"
    return selector.css(str_url).get()


def make_title(selector):
    str_title = "#js-article-title::text"
    return selector.css(str_title).get()


def make_timestamp(selector):
    str_timestamp = "#js-article-date::attr(datetime)"
    return selector.css(str_timestamp).get()


def make_writer(selector):
    str_writer = "*.z--font-bold a::text"
    writer = selector.css(str_writer).get()
    if writer is None:
        str_writer = "p.z--m-none.z--truncate.z--font-bold::text"
        writer = selector.css(str_writer).get()
    return writer.strip()


def make_shares(selector):
    str_shares = "div.tec--toolbar__item::text"
    shares_count = selector.css(str_shares).re_first(r"\d+")
    if shares_count is None:
        shares_count = 0
    return int(shares_count)


def make_comments(selector):
    str_comments = "#js-comments-btn::attr(data-count)"
    comments_count = selector.css(str_comments).get()
    if comments_count is None:
        comments_count = 0
    return int(comments_count)


def make_summary(selector):
    str_summary = ".tec--article__body > p:first-child *::text"
    summary = selector.css(str_summary).getall()
    return "".join(summary)


def make_sources(selector):
    str_sources = "div div.z--mb-16 div a::text"
    sources = selector.css(str_sources).getall()
    sources_formated = []
    for element in sources:
        sources_formated.append(element.strip())
    return sources_formated


def make_categories(selector):
    str_categories = "div div a.tec--badge.tec--badge--primary::text"
    categories = selector.css(str_categories).getall()
    categories_formated = []
    for element in categories:
        categories_formated.append(element.strip())
    return categories_formated


# Requisito 2
def scrape_noticia(html_content):
    selector = Selector(text=html_content)
    url = make_url(selector)
    title = make_title(selector)
    timestamp = make_timestamp(selector)
    writer = make_writer(selector)
    shares_count = make_shares(selector)
    comments_count = make_comments(selector)
    summary = make_summary(selector)
    sources = make_sources(selector)
    categories = make_categories(selector)
    return {
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


# Requisito 3
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    str_novidades = "div h3 a::attr(href)"
    return selector.css(str_novidades).getall()


# Requisito 4
def scrape_next_page_link(html_content):
    try:
        selector = Selector(text=html_content)
        next_1 = "#js-main > div > div > div.z--col.z--w-2-3 > "
        next_2 = "div.tec--list.tec--list--lg > a::attr(href)"
        str_next_page = next_1 + next_2
        return selector.css(str_next_page).get()
    except ValueError:
        return None


# Requisito 5
def get_tech_news(amount):
    html_base = fetch("https://www.tecmundo.com.br/novidades")
    news_url = scrape_novidades(html_base)
    if amount > 20 and amount <= 40:
        url_next_page = scrape_next_page_link(
            fetch("https://www.tecmundo.com.br/novidades")
        )
        html_next_page = fetch(url_next_page)
        news_url = scrape_novidades(html_base)
        next_page_url = scrape_novidades(html_next_page)
        for index in range(amount - 20):
            news_url.append(next_page_url[index])
    news = []
    for index in range(amount):
        fetch_news_html = fetch(news_url[index])
        get_news = scrape_noticia(fetch_news_html)
        news.append(get_news)
    create_news(news)
    return news
