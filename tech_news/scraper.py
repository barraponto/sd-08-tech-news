import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    """A função utiliza o método get() da biblioteca requests;
    Executada com uma URL correta retorna o conteúdo html;
    Sofrendo timeout, retorna None;
    Retorna None quando recebe uma resposta com código diferente de 200;
    Respeita o rate limit;"""

    try:
        response = requests.get(url, timeout=10)
        time.sleep(1)
        if response.status_code != 200:
            return None
        return response.text
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_noticia(html_content):
    """A função retorna o conteúdo correto e no formato correto,
    dada uma página de notícia."""

    selector = Selector(text=html_content)

    url = selector.css("head link[rel=canonical]::attr(href)").get()

    title = selector.css("#js-article-title::text").get()

    timestamp = selector.css("#js-article-date::attr(datetime)").get()

    writer = selector.css("#js-author-bar div p a::text").get()
    if writer:
        writer = writer.strip()

    shares_count = selector.css("#js-author-bar nav div::text").get()
    shares_count = shares_count and int(shares_count.split(" ")[1])

    comments_count = selector.css("#js-comments-btn::attr(data-count)").get()
    comments_count = comments_count and int(comments_count)

    summary = selector.css(
        "div.tec--article__body-grid > div > p:nth-child(1) *::text"
    ).getall()

    sources = selector.css("div.z--mb-16 div a::text").getall()
    for index in range(len(sources)):
        sources[index] = sources[index].strip()

    categories = selector.css("#js-categories a::text").getall()
    for index in range(len(categories)):
        categories[index] = categories[index].strip()

    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "shares_count": shares_count,
        "comments_count": comments_count,
        "summary": ''.join(summary),
        "sources": sources,
        "categories": categories,
    }


# Requisito 3
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
