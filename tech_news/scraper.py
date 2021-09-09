import requests
import time
from parsel import Selector
from tech_news.database import create_news


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


def scrape_news_url(selector):
    return selector.css(
        'link[rel="canonical"]::attr(href)').get()


def scrape_news_title(selector):
    return selector.css(
        '.tec--article__header__title::text').get()


def scrape_news_timestamp(selector):
    return selector.css('time::attr(datetime)').get()


def scrape_news_writer(selector):
    writer = (
        selector.css('.tec--author__info__link::text').get()
        if selector.css('.tec--author__info__link::text').get() is not None
        else selector.css('.tec--timestamp__item.z--font-bold > a::text').get()
    )
    if writer is None:
        writer = selector.css(
            '.z--m-none.z--truncate.z--font-bold::text').get()
    return writer.strip() if writer is not None else None


def scrape_news_share_count(selector):
    shares_count = selector.css(
        '.tec--toolbar__item::text').get()
    return (
        int(shares_count.strip().split()[0])
        if shares_count is not None else 0
    )


def scrape_news_comment_count(selector):
    comments_count = selector.css(
        '.tec--toolbar__item > button::attr(data-count)').re_first(r'\d+')
    return (
        int(comments_count) if comments_count is not None else 0
    )


def scrape_news_summary(selector):
    summarySelectors = selector.css(
        '.tec--article__body > p:first-child').css('*::text')
    summary = [selector.get() for selector in summarySelectors]
    summary = ''.join(summary)
    return summary


def scrape_news_sources(selector):
    sourcesSelectors = selector.css(
        'h2:contains("Fontes") + div').css('a::text')
    sources = [selector.get().strip() for selector in sourcesSelectors]
    return sources


def scrape_news_categories(selector):
    categoriesSelector = selector.css('#js-categories > a::text')
    categories = [selector.get().strip() for selector in categoriesSelector]
    return categories


# Requisito 2
def scrape_noticia(html_content):
    """Return the news info object of a html page content"""
    info_object = {}
    selector = Selector(html_content)

    info_object["url"] = scrape_news_url(selector)
    info_object["title"] = scrape_news_title(selector)
    info_object["timestamp"] = scrape_news_timestamp(selector)
    info_object["writer"] = scrape_news_writer(selector)
    info_object["shares_count"] = scrape_news_share_count(selector)
    info_object["comments_count"] = scrape_news_comment_count(selector)
    info_object["summary"] = scrape_news_summary(selector)
    info_object["sources"] = scrape_news_sources(selector)
    info_object["categories"] = scrape_news_categories(selector)

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
    """Return the url for the next news page"""
    selector = Selector(html_content)

    next_news_page_url = selector.css(
        '.tec--main .tec--list .tec--btn::attr(href)').get()
    return next_news_page_url


def scrape_news_from_newsList(news_url_list, news_array, amount_defined):
    for news_url in news_url_list:
        if len(news_array) < amount_defined:
            news_html_content = fetch(news_url)
            if news_html_content is not None:
                news_info = scrape_noticia(news_html_content)
                news_array.append(news_info)
        else:
            break


# Requisito 5
def get_tech_news(amount):
    """Return the amount input of news"""
    news = []
    url = 'https://www.tecmundo.com.br/novidades'
    while len(news) < amount:
        html_content = fetch(url)
        if html_content is not None:
            news_url_list = scrape_novidades(html_content)
            scrape_news_from_newsList(
                news_url_list=news_url_list,
                news_array=news,
                amount_defined=amount
            )
        url = scrape_next_page_link(html_content)
    create_news(news)
    return news
