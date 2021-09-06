import requests
import time
from parsel import Selector
from tech_news.database import create_news

# Referências:
# http://www.dannejaha.se/programming/google-and-seo/Na7d08fa2_cannonical/
# https://www.tabnine.com/code/java/packages/com.chimbori.crux.common
# https://www.w3schools.com/python/ref_string_strip.asp
# https://developer.mozilla.org/pt-BR/docs/Web/CSS/:nth-child


# Requisito 1
def fetch(url):
    """Seu código deve vir aqui"""
    try:
        response = requests.get(url, timeout=5)
        time.sleep(1)
        if response.status_code == 200:
            return response.text
    except requests.Timeout:
        return None


# Requisito 2
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""
    info = {}
    selector = Selector(html_content)

    info["url"] = selector.css("head link[rel=canonical]::attr(href)").get()

    info["title"] = selector.css(".tec--article__header__title::text").get()

    info["timestamp"] = selector.css("#js-article-date::attr(datetime)").get()

    info["writer"] = (
        selector.css(".z--font-bold").css("*::text").get().strip()
        if selector.css(".z--font-bold").css("*::text").get() is not None
        else None
    )

    info["shares_count"] = int(
        selector.css(".tec--toolbar__item::text").get().split()[0]
        if selector.css(".tec--toolbar__item::text").get() is not None
        else 0
    )

    info["comments_count"] = int(
        selector.css(".tec--toolbar__item .tec--btn::attr(data-count)").get()
        if selector.css(
            ".tec--toolbar__item .tec--btn::attr(data-count)"
        ).get() is not None
        else 0
    )

    info["summary"] = "".join(
        selector.css(".tec--article__body > p:nth-child(1) ::text").getall()
    )

    info["sources"] = [
        source.strip()
        for source in selector.css(
            ".z--mb-16 .tec--badge::text"
        ).getall()
    ]

    info["categories"] = [
        categorie.strip()
        for categorie in selector.css(
            "#js-categories .tec--badge::text"
        ).getall()
    ]

    return info


# Requisito 3
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(html_content)

    return selector.css("h3.tec--card__title a::attr(href)").getall()


# Requisito 4
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(html_content)

    response = selector.css(".tec--btn::attr(href)").get()
    if response:
        return response
    else:
        return None


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    urlBase = "https://www.tecmundo.com.br/novidades"
    techNews = list()

    while len(techNews) < amount:
        result = fetch(urlBase)
        urlsNovidades = scrape_novidades(result)
        for url in urlsNovidades:
            pageNoticia = scrape_noticia(fetch(url))
            if len(techNews) < amount:
                techNews.append(pageNoticia)

        urlBase = scrape_next_page_link(result)

    create_news(techNews)
    return techNews
