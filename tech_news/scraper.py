import requests
import time
from parsel import Selector
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    try:
        time.sleep(1)
        response = requests.get(url, timeout=3)
        if response.status_code == 200:
            return response.text

        return None
    except requests.exceptions.ReadTimeout:
        return None


# Requisito 2
def scrape_noticia(html_content):
    selector = Selector(text=html_content)

    categories = []
    sources = []
    share = 0
    writer = selector.css("a.tec--author__info__link::text").get()

    for categorie in selector.css("div#js-categories a::text").getall():
        categories.append(categorie.strip())

    for source in selector.css("div.z--mb-16 div a::text").getall():
        sources.append(source.strip())

    if selector.css("div.tec--toolbar__item::text").get():
        share = int(
          selector.css("div.tec--toolbar__item::text").get().split().pop(0)
        )

    if writer is None:
        writer = (
            selector
            .css("div.tec--timestamp__item a::Text").get()
        )

    dicionario = {
      "url": selector.css("head link[rel=canonical]::attr(href)").get(),
      "title": selector.css("h1.tec--article__header__title::text").get(),
      "timestamp": selector
      .css("div.tec--timestamp__item time::attr(datetime)").get(),
      "writer": writer,
      "shares_count": share,
      "comments_count": int(
        selector.css("div.tec--toolbar__item button::attr(data-count)").get()),
      "summary": ''.join(
        selector.css("div.tec--article__body p:nth-child(1) *::text").extract()
      ),
      "sources": sources,
      "categories": categories,
    }

    return dicionario


# Requisito 3
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    return selector.css("h3.tec--card__title a::attr(href)").getall()


# Requisito 4
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    return selector.css("a.tec--btn::attr(href)").get()


# Requisito 5
def get_tech_news(amount):
    URL_BASE = "https://www.tecmundo.com.br/novidades"
    index = 0
    array = []
    noticias = []

    while len(array) < amount:
        response = fetch(URL_BASE)

        for noticia in scrape_novidades(response):
            array.append(noticia)

        URL_BASE = scrape_next_page_link(response)

    while index < amount:
        html_noticia = fetch(array[index])
        noticia = scrape_noticia(html_noticia)
        create_news(noticia)
        noticias.append(noticia)
        index = index + 1

    return noticias
