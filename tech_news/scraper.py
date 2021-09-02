import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    time.sleep(1)

    try:
        response = requests.get(url, timeout=3)
    except requests.Timeout:
        return None

    if response.status_code == 200:
        return response.text
    else:
        return None


# Requisito 2
def scrape_noticia(html_content):
    result = {}
    selector = Selector(text=html_content)

    result["title"] = selector.css(".tec--article__header__title::text").get()
    result["url"] = selector.css("link[rel='canonical']::attr(href)").get()
    result["timestamp"] = selector.css(
        "#js-article-date::attr(datetime)"
    ).get()
    writer = selector.css(".tec--author__info__link::text").get()
    result["writer"] = writer.strip()
    shares_count = selector.css(".tec--toolbar__item::text").getall()
    shares_count = int(shares_count[0].split()[0])
    result["shares_count"] = shares_count

    comments_count = selector.css("#js-comments-btn::attr(data-count)").get()
    if comments_count is None:
        result["comments_count"] = 0
    else:
        result["comments_count"] = int(comments_count)

    summary = selector.css(
        ".tec--article__body > p:first-child *::text"
    ).getall()
    summary = "".join(summary)
    result["summary"] = summary

    sources = [
        source.strip()
        for source in selector.css(".z--mb-16 a.tec--badge::text").getall()
    ]
    result["sources"] = sources

    categories = [
        category.strip()
        for category in selector.css(
            "#js-categories a.tec--badge::text"
        ).getall()
    ]
    result["categories"] = categories

    return result


# Requisito 3
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    news_list = selector.css(
        "h3 a.tec--card__title__link::attr(href)"
    ).getall()
    return news_list


# Requisito 4
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    next_page_url = selector.css(
        "a.tec--btn.tec--btn--lg.tec--btn--primary::attr(href)"
    ).get()
    return next_page_url


teste = requests.get('https://www.tecmundo.com.br/novidades')
result = scrape_next_page_link(teste.text)
print(result)


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
