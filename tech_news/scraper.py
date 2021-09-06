from parsel import Selector
import requests
import time

# Referências:
# http://www.dannejaha.se/programming/google-and-seo/Na7d08fa2_cannonical/
# https://www.tabnine.com/code/java/packages/com.chimbori.crux.common
# https://www.w3schools.com/python/ref_string_strip.asp
# https://developer.mozilla.org/pt-BR/docs/Web/CSS/:nth-child


# Requisito 1
def fetch(url):
    """Seu código deve vir aqui"""
    try:
        response = requests.get(url, timeout=3)
        time.sleep(1)
        if response.status_code == 200:
            return response.text
    except requests.Timeout:
        return None


# Requisito 2
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(html_content)

    writer = selector.css(".tec--author__info__link::text").get()
    if writer:
        writer = writer.strip()
    else:
        writer = None

    shares_count = selector.css(".tec--toolbar__item::text").get().split()[0]
    if shares_count:
        shares_count = int(shares_count)
    else:
        shares_count = 0

    comments_count = selector.css(".tec--btn::text").get().split(" ")[0]
    if comments_count:
        comments_count = int(comments_count)
    else:
        comments_count = 0

    summary = selector.css(
        ".tec--article__body p:nth-child(1) ::text"
    ).getall()

    sources = selector.css(".z--mb-16 .tec--badge::text").getall()

    categories = selector.css("#js-categories .tec--badge::text").getall()

    info = {
        "url": selector.css("head link[rel=canonical]::attr(href)").get(),
        "title": selector.css(".tec--article__header__title::text").get(),
        "timestamp": selector.css("#js-article-date::attr(datetime)").get(),
        "writer": writer,
        "shares_count": shares_count,
        "comments_count": comments_count,
        "summary": "".join(summary),
        "sources": [source.strip() for source in sources],
        "categories": [categorie.strip() for categorie in categories]
    }
    return info


# Requisito 3
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(html_content)
    return selector.css("h3.tec--card__title a::attr(href)").getall()


# Requisito 4
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
