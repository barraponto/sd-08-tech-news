import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    time.sleep(1)
    try:
        request = requests.get(url, timeout=3)
        if request.status_code != 200:
            return None
        return request.text
    except requests.Timeout:
        return None


# Requisito 2
def scrape_noticia(html_content):
    selector = Selector(text=html_content)
    sources = selector.css('.z--mb-16 a::text').getall()
    sources = [source.strip() for source in sources]
    categories = selector.css('#js-categories a::text').getall()
    categories = [categorie.strip() for categorie in categories]
    return {
        "url": selector.css('link[rel=canonical]::attr(href)').get(),
        "title": selector.css('.tec--article__header__title ::text').get(),
        "timestamp": selector.css(
            '.tec--timestamp__item time::attr(datetime)').get(),
        "writer": selector.css(
            '.tec--author__info__link ::text').get().strip(),
        "shares_count": int(selector.css(
            '.tec--toolbar__item ::text').get().strip()[:1]),
        "comments_count": int(selector.css(
            '.tec--toolbar').re_first(r"\d+ Comentários").strip()[:1]),
        "summary": "".join(selector.css(
            '.tec--article__body p:first_child ::text').getall()),
        "sources": sources,
        "categories": categories,
    }


# Requisito 3
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    if selector:
        urls = selector.css('.tec--card__title__link ::attr(href)').getall()
        return urls[-20:]
    return []

print (scrape_novidades(fetch('https://www.tecmundo.com.br/novidades')))
# Requisito 4
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
