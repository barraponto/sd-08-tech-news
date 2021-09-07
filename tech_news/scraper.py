import requests
import time
from parsel import Selector

# Requisito 1


def fetch(url):
    time.sleep(1)
    try:
        response = requests.get(url, timeout=3)
        response.raise_for_status()
        return response.text
    except Exception:
        return None


# Requisito 2
def scrape_noticia(html_content):
    selector = Selector(text=html_content)
    news_link = selector.css("head link[rel=canonical]::attr(href)").get()
    news_title = selector.css("h1.tec--article__header__title::text").get()
    time = selector.css("div.tec--timestamp__item time::attr(datetime)").get()
    news_writer = selector.css("a.tec--author__info__link::text").get()
    if news_writer:
        news_writer = news_writer.strip()
    news_share = selector.css("div.tec--toolbar__item::text").get()
    if news_share:
        news_share = int((news_share.strip()).split(" ")[0])
    else:
        news_share = 0
    news_comments = selector.css("div.tec--toolbar__item::text").get()
    if news_comments:
        news_comments = int((news_comments.strip()).split(" ")[0])
    else:
        news_comments = 0
    news_summary = selector.css(
        ".tec--article__body p:first-child *::text"
    ).getall()
    news_source = selector.css(".z--mb-16 .tec--badge::text").getall()
    news_categories = selector.css("div#js-categories a::text").getall()

    return {
        "url": news_link,
        "title": news_title,
        "timestamp": time,
        "writer": news_writer,
        "shares_count": news_share,
        "comments_count": news_comments,
        "summary": "".join(news_summary),
        "sources": [source.strip() for source in news_source],
        "categories": [category.strip() for category in news_categories],
    }


# Requisito 3
def scrape_novidades(html_content):
    selector = Selector(html_content)
    get_links = selector.css(
        ".tec--list__item .tec--card__title__link::attr(href)"
    ).getall()
    if len(get_links) == 0:
        return []
    else:
        return get_links


# Requisito 4
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    next_page = selector.css("a.tec--btn ::attr(href)").get()
    return next_page or None


# Requisito 5
def get_tech_news(amount):
    news = []
    url = "https://www.tecmundo.com.br/novidades"

    get_url = fetch(url)
    get_links = scrape_novidades(get_url)

    while len(get_links) > 0:
        for i in range(amount):
            link = get_links[i]
            searching_news = fetch(link)
            if i > amount:
                details_news = scrape_noticia(searching_news)
                news.append(details_news)
        get_url = scrape_next_page_link(get_url)
        get_links = scrape_novidades(get_url)
    return news[:amount]
