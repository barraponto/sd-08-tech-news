import requests
import time
from parsel import Selector


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


# Requisito 2
def scrape_noticia(html_content):
    selector = Selector(text=html_content)

    def shares_count():
        if int(selector.css(".tec--toolbar__item::text")
                .get().split(" ")[1] != 0):
            return (
                int(
                    selector.
                    css(".tec--toolbar__item::text").get().split(" ")[1]))
        return 0

    def comments_count():
        if int(selector.css("#js-comments-btn::attr(data-count)").get() != 0):
            return (
                int(selector.css("#js-comments-btn::attr(data-count)").get()))
        return 0

    return({
            "url": selector.css("head link[rel='canonical']::attr(href)")
            .get(),

            "title": selector.css("head title::text").get().split("-")[0]
            .strip(),

            "timestamp": selector.css("#js-article-date::attr(datetime)")
            .get(),

            "writer": selector.css(".tec--author__info__link::text").get()
            .strip(),

            "shares_count": shares_count(),

            "comments_count": comments_count(),

            "summary": "".join(selector.css(
                ".tec--article__body p:first-child ::text"
            ).getall()),
            # https://www.simplilearn.com/tutorials/python-tutorial/list-to-string-in-python

            "sources": list(map(
                str.strip,
                (selector.css("div.z--mb-16 .tec--badge::text").getall()))),

            "categories": list(map(str.strip, selector.css(
                    "#js-categories a.tec--badge::text"
                ).getall())),
        })


scrape_noticia(fetch("https://www.tecmundo.com.br/mobilidade-urbana-smart-cities/155000-musk-tesla-carros-totalmente-autonomos.htm"))


# Requisito 3
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
