import requests
import time
from parsel import Selector
from tech_news.database import create_news

ONE_SECOND = 1
NEWS_URL = "https://www.tecmundo.com.br/novidades"


# Requisito 1
def fetch(url):
    try:
        time.sleep(ONE_SECOND)
        response = requests.get(url=url, timeout=ONE_SECOND*3)
        response.raise_for_status()
        return response.text
    except requests.Timeout:
        return None
    except requests.HTTPError:
        return None


# Requisito 2
def scrape_noticia(html_content):
    selector = Selector(text=html_content)

    url = selector.css("link[rel=canonical]::attr(href)").get()

    title = selector.css("#js-article-title::text").get()

    timestamp = selector.css("#js-article-date::attr(datetime)").get()

    writer = selector.css(".z--font-bold *::text").get()
    if writer is not None:
        writer = writer.strip() or ""

    shares_count = selector.css(".tec--toolbar__item::text").get()
    if shares_count is not None:
        shares_count = int(shares_count.split()[0].strip())
    else:
        shares_count = 0

    comments_count = selector.css("#js-comments-btn ::attr(data-count)").get()
    if comments_count is not None:
        comments_count = int(comments_count)
    else:
        comments_count = 0

    summary = "".join(
      selector.css(".tec--article__body > p:first-child *::text").getall()
    )

    sources = [
      source.strip() for source in selector.css(
        ".z--mb-16 .tec--badge::text").getall()
    ]

    categories = [
        category.strip() for category in selector.css(
          "#js-categories > a *::text").getall()
    ]

    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "shares_count": shares_count,
        "comments_count": comments_count,
        "summary": summary,
        "sources": sources,
        "categories": categories,
    }


# Requisito 3
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    return selector.css(
        "#js-main a.tec--card__title__link::attr(href)").getall()


# Requisito 4
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    return selector.css("a.tec--btn--primary::attr(href)").get()


# Requisito 5
def get_tech_news(amount):
    news_list = fetch(NEWS_URL)
    news_link = scrape_novidades(news_list)
    news = []
    is_filling = True

    while len(news) < amount:
        for link in news_link:
            news_page = fetch(link)
            news_content = scrape_noticia(news_page)
            news.append(news_content)
            if len(news) >= amount:
                is_filling = False
                break
        if not is_filling:
            break
        next_url = scrape_next_page_link(news_list)
        news_list = fetch(next_url)
        news_link = scrape_novidades(news_list)
    create_news(news)
    return news
