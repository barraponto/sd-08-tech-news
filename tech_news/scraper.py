import requests
import time
from parsel import Selector
from tech_news.database import create_news


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
def select_author(selector):
    writer = selector.css(".tec--author__info__link::text").get()

    if writer is None:
        writer = selector.css(
            ".tec--article__body-grid div div div div a::text"
        ).get()
        if writer is None:
            return None
        else:
            if writer == " ":
                return "Equipe TecMundo"
            else:
                return writer.strip()
    else:
        return writer.strip()


def scrape_noticia(html_content):
    result = {}
    selector = Selector(text=html_content)

    result["title"] = selector.css("#js-article-title::text").get()
    result["url"] = selector.css("link[rel='canonical']::attr(href)").get()
    result["timestamp"] = selector.css(
        "#js-article-date::attr(datetime)"
    ).get()

    result["writer"] = select_author(selector)

    shares_count = selector.css(".tec--toolbar__item::text").get()
    if shares_count is None:
        result["shares_count"] = 0
    else:
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
    result["summary"] = "".join(summary)

    result["sources"] = [
        source.strip()
        for source in selector.css(".z--mb-16 a.tec--badge::text").getall()
    ]

    result["categories"] = [
        category.strip()
        for category in selector.css(
            "#js-categories a.tec--badge::text"
        ).getall()
    ]

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


# Requisito 5
def get_tech_news(amount):
    URL = "https://www.tecmundo.com.br/novidades"

    html_content = fetch(URL)
    news_list = []

    while len(news_list) < amount:
        novidades_links = scrape_novidades(html_content)
        for link in novidades_links:
            if len(news_list) < amount:
                actual_noticia = fetch(link)
                noticia_html_content = scrape_noticia(actual_noticia)
                news_list.append(noticia_html_content)

        if len(news_list) < amount:
            next_link = scrape_next_page_link(html_content)
            html_content = fetch(next_link)

    create_news(news_list)
    return news_list

#  teste get_tech_news(5)
