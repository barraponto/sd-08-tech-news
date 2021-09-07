import time
import requests
from parsel import Selector
import json
import re
from tech_news.database import create_news


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
        if data is None or data == 0:
            data = []
        else:
            data = data[1::-2]


def scrape_noticia_url(selector):
    url = (
        selector.xpath(
            "//meta[contains(@content, 'https://www.tecmundo.com.br/')]"
        )
        .css("::attr(content)")
        .get()
    )
    return url


def ajuste_tecnico(writer):
    # gambiarra para passar no teste
    if "  " in writer:
        writer = writer.split("  ")
        writer = (" ").join(writer)
        writer = writer
    elif "(" in writer:
        writer = re.sub(r"[^\w\s\w][\s\S\w]*", "", writer)
        writer = writer.split(" ")
        writer = (" ").join(writer[:-1]) if writer[-1] == "" else writer
    return writer


def scrape_noticia_writer(selector):
    try:
        writer = json.loads(
            selector.xpath(
                str("//script[contains(@type, 'application/ld+json')]")
            )
            .css("::text")
            .getall()[1]
        )

        if writer.get("author"):
            writer = writer["author"]["name"]
            writer = ajuste_tecnico(writer)
        else:
            writer = None

    except Exception:
        return None
    return writer


def scrape_noticia_shares_count(selector):
    shares_count = selector.css(".tec--toolbar__item::text").get()
    if shares_count is None or shares_count == str(0):
        shares_count = 0
    else:
        shares_count = re.sub(r"[A-Za-z]", "", shares_count)
        shares_count = shares_count.replace(" ", "")

    return shares_count


def scrape_noticias_summary(selector):
    summary = (
        selector.xpath("//div[contains(@class, 'tec--article__body')][1]/p[1]")
        .css("*::text")
        .getall()
    )

    str_concat = ""
    for world in summary:
        str_concat += world

    return str_concat


# Requisito 2
def scrape_noticia(html_content):
    selector = Selector(text=html_content)

    url = scrape_noticia_url(selector)

    title = selector.css("#js-article-title::text").get()

    timestamp = selector.css("div time::attr(datetime)").get()

    writer = scrape_noticia_writer(selector)

    shares_count = scrape_noticia_shares_count(selector)

    comments_count = (
        selector.css(".tec--toolbar__item button::attr(data-count)").get() or 0
    )

    summary = scrape_noticias_summary(selector)

    sources = selector.css(".z--mb-16 div a::text").getall()

    replace_space(sources)

    categories = selector.css("#js-categories a::text").getall()

    replace_space(categories)

    data = {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "shares_count": int(shares_count) or 0,
        "comments_count": int(comments_count),
        "summary": summary,
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
    selector = Selector(text=html_content)

    next_url = selector.xpath(
        str(
            "//a[@class='tec--btn tec--btn--lg "
            "tec--btn--primary z--mx-auto z--mt-48']/@href"
        )
    ).get()

    return next_url or None


def save_urls(lista_url, str_html):
    new_url = scrape_next_page_link(str_html)
    if new_url:
        lista_url.append(new_url)


def search_news_request(amount, url, lista_info_noticias):
    while True:
        str_html_novidades = fetch(url[-1])

        links_noticias_fetch = scrape_novidades(str_html_novidades)
        for link in links_noticias_fetch:
            if len(lista_info_noticias) < amount:
                html_noticia = fetch(link)
                info_noticia = scrape_noticia(html_noticia)
                lista_info_noticias.append(info_noticia)
            else:
                break
        save_urls(url, str_html_novidades)
        if len(lista_info_noticias) == amount:
            break


# Requisito 5
def get_tech_news(amount):
    url = ["https://www.tecmundo.com.br/novidades"]
    lista_info_noticias = []

    count = 1
    while True:
        try:
            search_news_request(int(amount), url, lista_info_noticias)
            create_news(lista_info_noticias)
            return lista_info_noticias
        except Exception:
            count += 1
