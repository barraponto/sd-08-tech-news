import requests
import time
from parsel import Selector

# Requisito 1


def fetch(url):
    try:
        response = requests.get(url, timeout=3)
        time.sleep(1)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except requests.ReadTimeout:
        return


# Requisito 2
def scrape_noticia(html_content):
    notices = {}
    selector = Selector(html_content)

    notices["url"] = selector.css("link[rel='canonical']::attr(href)").get()
    title = selector.css(".tec--article__header__title::text").get()
    writer = selector.css(".tec--author__info__link::text").get().strip()
    notices["title"] = title
    timestamp = selector.css("time::attr(datetime)").get()
    notices["timestamp"] = timestamp
    if not writer:
        notices["writer"] = None
    else:
        notices["writer"] = writer
    shares_count = selector.css(".tec--toolbar__item::text").get()
    notices["shares_count"] = int(
        shares_count[: -len("Compartilharam")].strip()
        if shares_count is not None
        else 0
    )
    comments_count = selector.css("#js-comments-btn::attr(data-count)").get()
    notices["comments_count"] = (
        int(comments_count) if comments_count is not None else 0
    )
    summary_array = selector.css(
        "div.tec--article__body > p:nth-child(1) *::text"
    ).getall()
    summary = "".join(summary_array)
    notices["summary"] = summary
    source_array = selector.css("div.z--mb-16 > div > a::text").getall()
    sources = [sour.strip() for sour in source_array]
    notices["sources"] = sources
    categories_array = selector.css("#js-categories a::text").getall()
    categories = [categorie.strip() for categorie in categories_array]
    notices["categories"] = categories

    return notices


# Requisito 3
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    array_of_urls = selector.css(
        ".tec--list__item .tec--card__title__link::attr(href)"
    ).getall()
    return array_of_urls


# Requisito 4
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    next_page = selector.css(
        ".tec--btn.tec--btn--lg.tec--btn--primary"
        ".z--mx-auto.z--mt-48::attr(href)"
    ).get()
    return next_page


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
