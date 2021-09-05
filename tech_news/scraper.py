import requests
from tech_news.NewsDetailsScraper import NewsDetailsScraper
from tech_news.NewsScraper import NewsScraper
from tech_news.database import create_news
from ratelimit import limits, sleep_and_retry


# Requisito 1
@sleep_and_retry
@limits(calls=1, period=1)
def fetch(url):
    """
    Given a url returns the resulting html of the request
    Source: https://github.com/tomasbasham/ratelimit
    """
    try:
        response = requests.get(url, timeout=3)
        response.raise_for_status()
    except (requests.Timeout, requests.HTTPError):
        return None

    return response.text


# Requisito 2
def scrape_noticia(html_content):
    """Return news data as dict"""
    return NewsDetailsScraper(html_content).render()


# Requisito 3
def scrape_novidades(html_content):
    return NewsScraper(html_content).get_news_urls()


# Requisito 4
def scrape_next_page_link(html_content):
    return NewsScraper(html_content).get_next_page_url()


# Requisito 5
def get_tech_news(amount):
    page_url = "https://www.tecmundo.com.br/novidades"

    html_contents = []
    while True:
        root_html_content = fetch(page_url)
        scraper = NewsScraper(root_html_content)

        skip = amount - len(html_contents)
        urls = scraper.get_news_urls()[:skip]
        html_contents += [fetch(url) for url in urls]
        page_url = scraper.get_next_page_url()

        if len(html_contents) == amount:
            break

    news = [NewsDetailsScraper(html).render() for html in html_contents]
    create_news(news[:amount])
    return news[:amount]
