import requests
import time
from parsel import Selector
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    try:
        response = requests.get(url)
        time.sleep(2)
        if (response.status_code == 200):
            return response.text
        pass
    except requests.ReadTimeout:
        pass


def shares_count(html_content):
    selector = Selector(text=html_content)
    if (selector.css(".tec--toolbar__item::text")
            .get() is None):
        return 0
    if int(selector.css(".tec--toolbar__item::text")
            .get().strip().split(" ")[0] != 0):
        return (
            int(
                selector.
                css(".tec--toolbar__item::text").get()
                .strip().split(" ")[0]))
    return 0


def comments_count(html_content):
    selector = Selector(text=html_content)
    if int(selector.css("#js-comments-btn::attr(data-count)").get() != 0):
        return (
            int(selector.css("#js-comments-btn::attr(data-count)").get()))
    return 0


def writer(html_content):
    selector = Selector(text=html_content)
    data_1 = selector.css(".tec--author__info__link::text").get()
    data_2 = selector.css("a[href*=autor]::text").get()
    # https://developer.mozilla.org/en-US/docs/Web/CSS/Attribute_selectors
    data_3 = selector.css(".tec--author__info p::text").get()

    if data_1:
        return data_1.strip() if data_1 else None
    if data_2:
        return data_2.strip() if data_2 else None
    if data_3:
        return data_3.strip() if data_3 else None


# Requisito 2
def scrape_noticia(html_content):
    selector = Selector(text=html_content)

    return({
            "url": selector.css("head link[rel='canonical']::attr(href)")
            .get(),

            "title": selector.css("#js-article-title::text").get(),

            "timestamp": selector.css("#js-article-date::attr(datetime)")
            .get(),

            "writer": writer(html_content),

            "shares_count": shares_count(html_content),

            "comments_count": comments_count(html_content),

            "summary": "".join(selector.css(
                ".tec--article__body > p:first-child ::text"
            ).getall()),
            # https://www.simplilearn.com/tutorials/python-tutorial/list-to-string-in-python

            "sources": list(map(
                str.strip,
                (selector.css("div.z--mb-16 .tec--badge::text").getall()))),

            "categories": list(map(str.strip, selector.css(
                    "#js-categories a.tec--badge::text"
                ).getall())),
        })


# Requisito 3
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    return selector.css("h3 .tec--card__title__link::attr(href)").getall()


# Requisito 4
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    return selector.css("a.tec--btn::attr(href)").get()


# Requisito 5
def get_tech_news(amount):
    teste_array = []
    url = "https://www.tecmundo.com.br/novidades"
    data_novidades_links = scrape_novidades(
        fetch(url))[:amount]
    for i in data_novidades_links:
        print(i)
        teste_array.append(scrape_noticia(fetch(i)))
    create_news(teste_array)
    return teste_array
