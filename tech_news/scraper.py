import requests
from parsel import Selector
import time

from tech_news.database import create_news


# Requisito 1
def fetch(url):
    time.sleep(1)
    try:
        response = requests.get(url, timeout=3)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except requests.Timeout:
        return None


def get_writer(categories, selector):
    if "Minha Série" not in categories:
        return selector.css(".tec--author__info *::text").get().strip()
    else:
        return selector.css(
            "#js-main > div > article > div>"
            "div > div > div > div > a::text").get().strip()


def get_shares_count(categories, selector):
    if "Minha Série" not in categories and "Voxel" not in categories:
        return int(selector.css(
            '.tec--toolbar > div:nth-child(1)::text').get().split()[0])
    else:
        return 0


# Requisito 2
def scrape_noticia(html_content):
    selector = Selector(html_content)

    url = [
        selected.css("link::attr(href)").get()
        for selected in selector.css("head > link")
        if selected.css("link::attr(rel)").get() == "canonical"][0]

    title = selector.css("#js-article-title::text").get()

    timestamp = selector.css("#js-article-date::attr(datetime)").get()

    categories = selector.css("#js-categories > a::text").getall()
    categories = [category.strip() for category in categories]

    summary = ''.join(
        selector.css(".tec--article__body > p:nth-child(1) *::text").getall())

    sources = selector.css(".z--mb-16 > div > a::text").getall()
    sources = [source.strip() for source in sources]

    comments_count = int(selector.css(
        '#js-comments-btn::attr(data-count)').get())

    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": get_writer(categories, selector),
        "shares_count": get_shares_count(categories, selector),
        "comments_count": comments_count,
        "summary": summary,
        "sources": sources,
        "categories": categories
    }


# Requisito 3
def scrape_novidades(html_content):
    selector = Selector(html_content)
    urls = selector.css("article > div > h3 > a::attr(href)").getall()
    return [url.strip() for url in urls]


# Requisito 4
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    return selector.css(
        "#js-main > div > div > div > div> a::attr(href)").get()


# Requisito 5
def get_tech_news(amount):
    path = "https://www.tecmundo.com.br/novidades"
    news = []
    while len(news) < amount and path:
        html_news = fetch(path)
        url_news_per_page = scrape_novidades(html_news)
        for url in url_news_per_page:
            if len(news) < amount:
                html_specif_news = fetch(url)
                news.append(scrape_noticia(html_specif_news))
        path = scrape_next_page_link(html_news)
    create_news(news)
    return news
