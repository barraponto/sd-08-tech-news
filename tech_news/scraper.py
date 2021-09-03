import time
import requests
from parsel import Selector
from tech_news.database import create_news
from math import ceil


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


def get_writer(selector):
    writer = selector.css(".tec--author__info__link::text").get()
    if writer:
        return writer.strip()
    else:
        writer = selector.css(
            ".tec--article__body-grid div div div div a::text"
        ).get()
        if writer:
            if (writer == ' '):
                return "Equipe TecMundo"
            else:
                return writer.strip()


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
    dic_new['writer'] = get_writer(selector)

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
    selector = Selector(text=html_content)
    return selector.css(
      "div.tec--list a.tec--btn::attr(href)"
    ).get()


# Requisito 5
def get_tech_news(amount):
    scraped_news = []

    page_news = fetch("https://www.tecmundo.com.br/novidades")
    links_news = scrape_novidades(page_news)

    count_pages = ceil(amount / 20)

    if count_pages > 1:
        for _ in range(1, count_pages):
            page_news = scrape_next_page_link(page_news)
            next_page = fetch(page_news)
            next_page_news = scrape_novidades(next_page)
            links_news = links_news + next_page_news

    for link in links_news:
        news = fetch(link)
        scraped_news.append(scrape_noticia(news))
        if len(scraped_news) == amount:
            break

    create_news(scraped_news)
    return scraped_news
