import time
import requests
from parsel import Selector


# Requisito 1
def fetch(url):
    try:
        response = requests.get(url, timeout=3)
        time.sleep(1)

        if (response.status_code == 200):
            return response.text

        return None
    except requests.ReadTimeout:
        return None


def isExist(new):
    if new:
        return True
    return False


# Requisito 2
def scrape_noticia(html_content):
    dic_new = {}
    new = ""
    selector = Selector(text=html_content)

    dic_new['url'] = selector.css(
        "meta[property='og:url']::attr(content)"
        ).get()

    dic_new['title'] = selector.css(".tec--article__header__title::text").get()
    dic_new['timestamp'] = selector.css("time::attr(datetime)").get()

    new = selector.css(".tec--author__info__link::text").get()
    if isExist(new):
        dic_new['writer'] = new.strip()

    new = selector.css(".tec--toolbar__item::text").get()
    if isExist(new):
        dic_new['shares_count'] = int(new.split(' ')[1])
    else:
        dic_new['shares_count'] = 0

    new = selector.css("#js-comments-btn::attr(data-count)").get()
    if isExist(new):
        dic_new['comments_count'] = int(new)
    else:
        dic_new['comments_count'] = 0

    dic_new['summary'] = "".join(selector.css(
        ".tec--article__body > p:first-child *::text"
    ).getall())

    dic_new['sources'] = list(map(str.strip, selector.css(
        ".z--mb-16 div a.tec--badge::text"
    ).getall()))

    dic_new['categories'] = list(map(str.strip, selector.css(
        "div#js-categories a.tec--badge::text"
    ).getall()))

    return dic_new


# Requisito 3
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    return selector.css(
      "h3.tec--card__title a.tec--card__title__link::attr(href)"
    ).getall()


# Requisito 4
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
