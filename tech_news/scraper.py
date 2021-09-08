import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    """Get html of a page from url"""
    time.sleep(1)
    try:
        response = requests.get(url, timeout=3)
        response.raise_for_status()
    except (requests.Timeout, requests.HTTPError):
        return None
    return response.text


# Requisito 2
def scrape_noticia(html_content):
    """Return the news info object of a html page content"""
    info_object = {}
    selector = Selector(html_content)

    url = selector.css('link[rel="canonical"]::attr(href)').get()
    info_object["url"] = url

    title = selector.css('.tec--article__header__title::text').get()
    info_object["title"] = title

    timestamp = selector.css('time::attr(datetime)').get()
    info_object["timestamp"] = timestamp

    writer = selector.css('.tec--author__info__link::text').get()
    info_object["writer"] = writer.strip() if writer is not None else None

    shares_count = selector.css('.tec--toolbar__item::text').re_first('d+')
    info_object["shares_count"] = (
        int(shares_count) if shares_count is not None else 0
    )

    comments_count = selector.css(
        '.tec--toolbar__item > button::text').re_first(r'\d+')
    info_object["comments_count"] = int(comments_count)

    summarySelectors = selector.css(
        '.tec--article__body p:first-child').css('*::text')
    summary = [selector.get() for selector in summarySelectors]
    summary = ''.join(summary)
    info_object["summary"] = summary

    sourcesSelectors = selector.css(
        'h2:contains("Fontes") + div').css('a::text')
    sources = [selector.get().strip() for selector in sourcesSelectors]
    info_object["sources"] = sources

    categoriesSelector = selector.css('#js-categories > a::text')
    categories = [selector.get().strip() for selector in categoriesSelector]
    info_object["categories"] = categories

    return info_object


# Requisito 3
def scrape_novidades(html_content):
    """Returns a list of urls for recent news"""
    selector = Selector(html_content)

    news_url_list_selectors = selector.css(
        '.tec--main .tec--card__title__link::attr(href)')
    news_url_list = (
        [selector.get() for selector in news_url_list_selectors
            if selector is not None]
    )
    return news_url_list


# Requisito 4
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
