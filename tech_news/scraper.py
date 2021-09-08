from tech_news.database import create_news
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

    # Solução desenvovida pela Aline Debastiani - Turma 8
    # https://github.com/tryber/sd-08-tech-news/blob/aline-tech-news/tech_news/scraper.py
    url = selector.css("head link[rel=canonical]::attr(href)").get()

    title = selector.css("#js-article-title::text").get()

    timestamp = selector.css("#js-article-date::attr(datetime)").get()

    # Solução desenvovida pelo Erik Massaki - Turma 8
    # https://github.com/tryber/sd-08-tech-news/blob/eric-massaki-tech-news-project/tech_news/scraper.py
    writer = selector.css(".z--font-bold *::text").get()
    if writer:
        writer = writer.strip()

    shares_count = selector.css("nav.tec--toolbar div::text").get()
    shares_count = shares_count and int(shares_count.split(" ")[1])
    if not shares_count:
        shares_count = 0

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
        "summary": "".join(summary),
        "sources": sources,
        "categories": categories,
    }


# Requisito 3
def scrape_novidades(html_content):
    """A função retorna os dados esperados quando chamada com os parâmetros
    corretos; Retorna uma lista vazia quando chamada com parâmetros
    incorretos"""

    selector = Selector(text=html_content)

    return selector.css(".tec--list div article div h3 a::attr(href)").getall()


# Requisito 4
def scrape_next_page_link(html_content):
    """A função retorna os dados esperados quando chamada com os
    parâmetros corretos; Retorna None quando chamada com os parâmetros
    incorretos"""

    selector = Selector(text=html_content)
    return selector.css(".tec--btn.tec--btn--lg::attr(href)").get()


# Requisito 5
def get_tech_news(amount):
    """A função create_news do tech_news/database.py é chamada corretamente;
    Retorna a quantidade correta de notícias"""

    html_content = fetch("https://www.tecmundo.com.br/novidades")

    news_urls = scrape_novidades(html_content)

    data_news = []

    for index in range(amount):
        index_factor = 0

        if index >= len(news_urls):
            next_page_url = scrape_next_page_link(html_content)
            next_page_html_content = fetch(next_page_url)
            news_urls = scrape_novidades(next_page_html_content)
            index_factor = index - 1

        new_html_content = fetch(news_urls[index - index_factor])
        single_data_new = scrape_noticia(new_html_content)
        data_news.append(single_data_new)

    create_news(data_news)

    return data_news
