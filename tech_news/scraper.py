import requests
from parsel import Selector
import time


# Requisito 1
def fetch(url):
    time.sleep(1)

    try:
        response = requests.get(url, timeout=3)
    except (
        requests.exceptions.HTTPError,
        requests.exceptions.TooManyRedirects,
        requests.exceptions.Timeout,
        requests.exceptions.ConnectionError,
    ):
        return None

    if response.status_code != 200:
        return None

    return response.text


# Requisito 2
def scrape_noticia(html_content):
    news = {}
    selector = Selector(text=html_content)

    url = selector.css("link[rel='canonical']::attr(href)").get()
    news["url"] = url

    title = selector.css(".tec--article__header__title::text").get()
    news["title"] = title

    timestamp = selector.css("#js-article-date::attr(datetime)").get()
    news["timestamp"] = timestamp

    writer = selector.css(".tec--author__info__link::text").get()
    news["writer"] = writer.strip()

    shares_count = selector.css(".tec--toolbar__item::text").getall()
    shares_count = int(shares_count[0].split()[0])
    news["shares_count"] = shares_count

    comments_count = selector.css("#js-comments-btn::attr(data-count)").get()
    if comments_count is None:
        news["comments_count"] = 0
    else:
        news["comments_count"] = int(comments_count)

    summary = selector.css(
        ".tec--article__body > p:first-child *::text"
    ).getall()
    # source: https://pt.stackoverflow.com/questions/324979/como-concatenar
    # -itens-de-uma-lista-em-python
    summary = "".join(summary)
    news["summary"] = summary

    sources = selector.css(".z--mb-16 a.tec--badge::text").getall()
    sources = [source.strip() for source in sources]
    news["sources"] = sources

    categories = selector.css("#js-categories a.tec--badge::text").getall()
    categories = [category.strip() for category in categories]
    news["categories"] = categories

    return news


# Requisito 3
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    news = selector.css("h3 .tec--card__title__link::attr(href)").getall()
    print(news)
    return news


# Requisito 4
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
