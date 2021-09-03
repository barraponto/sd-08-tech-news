from time import sleep
import requests
from parsel import Selector
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    """Seu código deve vir aqui"""
    sleep(1)
    try:
        html = requests.get(url, timeout=3)
    except requests.Timeout:
        return None
    if html.status_code != 200:
        return None
    return html.text


# Requisito 2
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)

    categories_raw = selector.css("div#js-categories a::text").getall()
    sources_raw = selector.css(".z--mb-16 > div > a::text").getall()
    try:
        writer_raw = (
            selector.css(".tec--timestamp__item.z--font-bold *::text")
            .get()
            .strip()
        )
    except AttributeError:
        writer_raw = (
            selector.css(".tec--author__info *::text").get().strip()
        )
    try:
        shares_count_raw = int(
            selector.css(".tec--toolbar__item::text")
            .getall()[0]
            .strip()
            .split(" ")[0]
        )
    except IndexError:
        shares_count_raw = 0

    try:
        comments_count_raw = int(
            selector.css(".tec--toolbar > div.tec--toolbar__item *::text")
            .get()
            .strip()
            .split(" ")[0]
        )
    except ValueError:
        comments_count_raw = 0

    return {
        "url": selector.css('meta[property="og:url"]::attr("content")').get(),
        "title": selector.css(".tec--article__header__title::text").get(),
        "timestamp": selector.css(
            ".tec--timestamp__item > time::attr(datetime)"
        ).get(),
        "writer": writer_raw,
        "shares_count": shares_count_raw,
        "comments_count": comments_count_raw,
        "summary": "".join(
            selector.css(
                ".tec--article__body > p:nth-of-type(1) *::text"
            ).getall()
        ).strip(),
        "sources": [source.strip() for source in sources_raw],
        "categories": [category.strip() for category in categories_raw],
    }


# Requisito 3
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    return selector.css(
        ".tec--list__item  .tec--card__title__link::attr(href)"
    ).getall()


# Requisito 4
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    return selector.css(
        ".tec--btn.tec--btn--lg"
        ".tec--btn--primary.z--mx-auto.z--mt-48::attr(href)"
    ).get()


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    url = "https://www.tecmundo.com.br/novidades"
    news_dict_list = []
    while len(news_dict_list) <= amount:
        current_page_content = fetch(url)
        urls_to_scrape = scrape_novidades(current_page_content)
        for url in urls_to_scrape:
            content = fetch(url)
            news = scrape_noticia(content)
            news_dict_list.append(news)
            if len(news_dict_list) >= amount:
                break
        url = scrape_next_page_link(current_page_content)
    create_news(news_dict_list)
    return news_dict_list[-amount:]
