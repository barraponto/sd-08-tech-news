import requests
from parsel import Selector
import time


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


# Requisito 2
def scrape_noticia(html_content):
    selector = Selector(html_content)

    url = [
        selected.css("link::attr(href)").get()
        for selected in selector.css("head > link")
        if selected.css("link::attr(rel)").get() == "canonical"][0]

    title = selector.css("#js-article-title::text").get()

    timestamp = selector.css("#js-article-date::attr(datetime)").get()

    writer = selector.css(".tec--author__info__link::text").get().strip()

    summary = ''.join(
        selector.css(".tec--article__body > p:nth-child(1) *::text").getall())

    sources = selector.css(".z--mb-16 > div > a::text").getall()
    sources = [source.strip() for source in sources]

    categories = selector.css("#js-categories > a::text").getall()
    categories = [category.strip() for category in categories]

    shares_count = int(selector.css(
        '.tec--toolbar > div:nth-child(1)::text').get().split()[0])

    comments_count = int(selector.css(
        '#js-comments-btn::attr(data-count)').get())

    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "shares_count": shares_count,
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
    """Seu código deve vir aqui"""
