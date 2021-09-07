from parsel import Selector
from math import ceil
import requests
import time
from tech_news.database import create_news
from pprint import pprint


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
    writer = selector.css("#js-author-bar > div > p > a::text").get()
    if writer is None:
        writer = selector.css(
            "#js-main > div > article > div.tec--article__body-grid >"
            "div.z--pt-40.z--pb-24 > div.z--flex.z--items-center >"
            "div.tec--timestamp.tec--timestamp--lg > div.tec--timestamp__item."
            "z--font-bold > a::text"
        ).get()
    shares_count = selector.css(
        "#js-author-bar > nav > div:nth-child(1)::text"
    ).get()
    if shares_count is None:
        shares_count = 0
    else:
        shares_count = int(shares_count.split(" ", 2)[1])
    comments_count = selector.css("#js-comments-btn::attr(data-count)").get()
    summary = selector.css(
        "div.tec--article__body > p:nth-child(1) *::text"
    ).getall()
    sources = selector.css(
        "#js-main > div.z--container > article > div.tec--article__body-grid >"
        "div.z--mb-16.z--px-16 > div > a::text"
    ).getall()
    categories = selector.css("a.tec--badge--primary ::text").getall()
    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer.strip(),
        "shares_count": shares_count,
        "comments_count": int(comments_count),
        "summary": "".join(summary),
        "sources": [i.strip() for i in sources],
        "categories": [i.strip() for i in categories],
    }
    # pprint(obj)
    # return obj


# Requisito 3
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    return selector.css("#js-main h3 a::attr(href)").getall()


# Requisito 4
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    return selector.css(
        "#js-main > div > div > div.z--col.z--w-2-3 >"
        "div.tec--list.tec--list--lg > a::attr(href)"
    ).get()


# Requisito 5
def get_tech_news(amount):
    # """Seu código deve vir aqui"""
    url = "https://www.tecmundo.com.br/novidades"
    lista_noticias = []
    pagina = fetch(url)
    lista_url = scrape_novidades(pagina)
    for _ in range(ceil(amount / 20)):
        size = 20 if amount >= 20 else amount - 20
        for link in lista_url[:size]:
            noticia = fetch(link)
            conteudo = scrape_noticia(noticia)
            lista_noticias.append(conteudo)
        amount -= 20
        proxima = scrape_next_page_link(url)
        lista_url = scrape_novidades(proxima)
    create_news(lista_noticias)
    return lista_noticias
