import time
import requests
from parsel import Selector
import json
import re


def fetch(url):
    try:
        time.sleep(1)
        html = requests.get(url, timeout=3)
        if html.status_code == 200:
            return html.text
        else:
            return None
    except requests.ReadTimeout:
        return None


def replace_space(data):
    if len(data) > 0:
        for x in range(len(data)):
            data[x] = data[x][1:-1]
    else:
        data = data[1::-2]


# Requisito 2
def scrape_noticia(html_content):
    selector = Selector(text=html_content)

    url = (
        selector.xpath(
            "//meta[contains(@content, 'https://www.tecmundo.com.br/')]"
        )
        .css("::attr(content)")
        .get()
    )

    title = selector.css("#js-article-title::text").get()

    timestamp = selector.css("div time::attr(datetime)").get()

    writer = json.loads(
        (
            selector.xpath(
                str("//script[contains(@type, 'application/ld+json')]")
            )
            .css("::text")
            .getall()[1]
        )
    )["author"]["name"]

    shares_count = re.sub(
        r"[A-Za-z]", "", selector.css(".tec--toolbar__item::text").get()
    )

    comments_count = selector.css(
        ".tec--toolbar__item button::attr(data-count)"
    ).get()

    summary = (
        selector.xpath("//div[contains(@class, 'tec--article__body')][1]/p[1]")
        .css("*::text")
        .getall()
    )

    str_concat = ""
    for world in summary:
        str_concat += world

    sources = selector.css(".z--mb-16 div a::text").getall()

    replace_space(sources)

    categories = selector.css("#js-categories a::text").getall()

    replace_space(categories)

    data = {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "shares_count": int(shares_count.replace(" ", "")) or 0,
        "comments_count": int(comments_count) or 0,
        "summary": str_concat,
        "sources": sources,
        "categories": categories,
    }

    return data


# Requisito 3
def scrape_novidades(html_content):
    selector = Selector(text=html_content)

    list_links_noticias = selector.xpath(
        str(
            "//div[@class='tec--list__item']"
            "//figure//a[@class='tec--card__thumb__link']/@href"
        )
    ).getall()

    if len(list_links_noticias) == 0:
        return []

    return list_links_noticias


# Requisito 4
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
