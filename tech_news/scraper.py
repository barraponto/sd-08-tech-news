import requests
import time
from parsel import Selector
from tech_news.database import create_news

BASE_URL = "https://www.tecmundo.com.br/novidades"


# Requisito 1
def fetch(url):
    time.sleep(1)
    try:
        response = requests.get(url, timeout=3)
        if response.status_code != 200:
            return None
        return response.text
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_noticia(html_content):
    selector = Selector(text=html_content)
    url = selector.css("link[rel=canonical]::attr(href)").get()
    title = selector.css("#js-article-title::text").get()
    timestamp = selector.css("#js-article-date::attr(datetime)").get()
    writer = selector.css(".tec--article__body-grid .z--font-bold *::text") \
        .get().strip()
    shares_count = int(selector
                       .css(".tec--toolbar__item:not(:last-child) *::text")
                       .re_first(r"\d+", default=0))
    comments_count = int(selector.css("#js-comments-btn *::text")
                         .re_first(r"\d+", default=0))
    summary = ''.join(selector
                      .css(".tec--article__body > p:first-child *::text")
                      .getall())
    sources = selector.css("div:not(#js-categories) > a.tec--badge::text") \
                      .re(r"\S.*\S")
    categories = selector.css("#js-categories a::text").re(r"\S.*\S")
    return {"url": url, "title": title, "timestamp": timestamp,
            "writer": writer,
            "shares_count": shares_count, "comments_count": comments_count,
            "summary": summary,
            "sources": sources, "categories": categories}


# Requisito 3
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    return selector.css(".tec--list__item h3 a::attr(href)").getall()


# Requisito 4
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    return selector.css(".tec--list > a::attr(href)").get()


# Requisito 5
def get_tech_news(amount):
    news = []
    next_page = BASE_URL
    while (len(news) < amount and next_page):
        resp = fetch(next_page)
        novidades = scrape_novidades(resp)[0:amount - len(news)]
        novidades_html = [fetch(noticia) for noticia in novidades]
        curr_page_news = [scrape_noticia(novidade_html)
                          for novidade_html in novidades_html]
        news.extend(curr_page_news)
        next_page = scrape_next_page_link(resp)
    create_news(news)
    return news
