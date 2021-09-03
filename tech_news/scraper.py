from parsel import Selector
import requests
import time


# Requisito 1
def fetch(url):
    time.sleep(1)
    try:
        response = requests.get(
            url, headers={"Accept": "application/json"}, timeout=3
        )
    except Exception:
        return None
    if response.status_code == 200:
        return response.text
    return None


# Requisito 2
def scrape_noticia(html_content):
    selector = Selector(text=html_content)
    url = selector.css("head > link:nth-child(26)::attr(href)").get()
    title = selector.css("#js-article-title::text").get()
    timestamp = selector.css("#js-article-date::attr(datetime)").get()
    writer = selector.css(
        "#js-author-bar > div > p.z--m-none.z--truncate.z--font-bold > a::text"
    ).get()
    shares_count = selector.css(
        "#js-author-bar > nav > div:nth-child(1)::text"
    ).get()
    comments_count = selector.css("#js-comments-btn::attr(data-count)").get()
    summary = selector.css(
        "div.tec--article__body > p:nth-child(1)::text"
    ).getall()
    sources = selector.css(
        "#js-main > div.z--container > article > div.tec--article__body-grid >"
        "div.z--mb-16.z--px-16 > div > a::text"
    ).getall()
    categorie = selector.css("#js-categories::text").getall()
    categories = selector.css("a.tec--badge--primary ::text").getall()
    categories = []
    for i in categorie:
        j = i.strip()
        categories.append(j)
    print(url)
    print(title)
    print(timestamp)
    if not (writer):
        None
    print(writer)
    if not (shares_count):
        0
    print(shares_count)
    print(comments_count)
    print("".join(summary))
    print("".join(sources))
    print(categories)


# Requisito 3
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
