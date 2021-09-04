import requests
import time
from parsel import Selector
from tech_news.database import create_news


def scrape_author(selector):
    """Scrape the author from a tech news"""
    writer = selector.css(".tec--author__info__link::text").get()
    if not writer:
        writer = selector.css(
            ".tec--article__body-grid div div div div a::text"
        ).get()
        if not writer:
            writer = " "
    if writer == " ":
        writer = "Equipe TecMundo"
    return writer.strip()


def scrape_shares_count(selector):
    """Scrape the number of shares the tech news has"""
    shares_count = selector.css(".tec--toolbar__item::text").get()
    if not shares_count:
        shares_count = 0
    else:
        shares_count = shares_count.strip().split(" ")[0]
    return int(shares_count)


def scrape_comments_count(selector):
    """Scrape the number of comments the tech news has"""
    comments_count = selector.css(
        "button#js-comments-btn::attr(data-count)"
    ).get()
    if not comments_count:
        comments_count = 0
    return int(comments_count)


# Requisito 1
def fetch(url):
    """Returns an url content with a rate limit of 1 request per second
    and timeout of 3 seconds for each
    """
    try:
        time.sleep(1)
        response = requests.get(url, timeout=3)
        if response.status_code != 200:
            return None
        return response.text
    except requests.exceptions.Timeout:
        return None


# Requisito 2
def scrape_noticia(html_content):
    """Returns a dict with the selected info from a html content"""
    if not html_content:
        return None
    selector = Selector(text=html_content)

    return {
        "url": selector.css('link[rel="canonical"]::attr(href)').get(),
        "title": selector.css("h1#js-article-title::text").get(),
        "timestamp": (
            selector.css(".tec--timestamp__item")
            .xpath("./time/@datetime")
            .get()
        ),
        "writer": scrape_author(selector),
        "shares_count": scrape_shares_count(selector),
        "comments_count": scrape_comments_count(selector),
        "summary": selector.css(".tec--article__body")
        .xpath("string(./p)")
        .get(),
        "sources": [
            source.strip()
            for source in selector.xpath('//h2[text() = "Fontes"]/..')
            .css(".tec--badge ::text")
            .getall()
        ],
        "categories": [
            category.strip()
            for category in selector.css(
                "div#js-categories > a::text"
            ).getall()
        ],
    }


# Requisito 3
def scrape_novidades(html_content):
    """Returns a list of urls for the articles in the given html_content."""
    if not html_content:
        return []
    selector = Selector(text=html_content)
    return selector.css("div.tec--card__info > h3 > a::attr(href)").getall()


# Requisito 4
def scrape_next_page_link(html_content):
    """Returns the link to next page of contents if there are more."""
    selector = Selector(text=html_content)
    response = selector.css("div.tec--list > a::attr(href)").get()
    if not response:
        return None
    return response


# Requisito 5
def get_tech_news(amount):
    """Returns the list of tech news scraped and insert it into DB."""
    TECMUNDO_NOVIDADES_URL = "https://www.tecmundo.com.br/novidades"
    news_urls_list = []

    novidades_html = fetch(TECMUNDO_NOVIDADES_URL)
    news_urls_list.extend(scrape_novidades(novidades_html))

    while True:
        if len(news_urls_list) < amount:
            next_page_url = scrape_next_page_link(novidades_html)
            novidades_html = fetch(next_page_url)
            news_urls_list.extend(scrape_novidades(novidades_html))
        else:
            break

    news_list = []
    for news_url in news_urls_list[:amount]:
        news = scrape_noticia(fetch(news_url))
        news_list.append(news)

    create_news(news_list)
    return news_list
