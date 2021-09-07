import requests
import time
import math
from parsel import Selector

from tech_news.database import create_news
from tech_news.utils.scrape_helper import (
    scrape_news_writer, scrape_news_shares_count, scrape_news_comments_count
)


def fetch(url):
    try:
        response = requests.get(url, timeout=3)
        if response.status_code == 200:
            return response.text
    except (requests.ReadTimeout, requests.ConnectionError):
        return None

    time.sleep(1)


def scrape_noticia(html_content):
    selector = Selector(text=html_content)

    news_data_dict = {
      'url': selector.css('link[rel="canonical"]::attr(href)').get(),
      'title': selector.css('#js-article-title::text').get(),
      'timestamp': selector.css('#js-article-date::attr(datetime)').get(),
      'writer': scrape_news_writer(html_content),
      'shares_count': scrape_news_shares_count(html_content),
      'comments_count': scrape_news_comments_count(html_content),
      'summary': ''.join(
          selector.css('.tec--article__body > p:first-child *::text').getall()
      ),
      'sources': [
          source.strip() for source in
          selector.css('.z--mb-16 .tec--badge::text').getall()
      ],
      'categories': [
          category.strip() for category
          in selector.css('#js-categories .tec--badge::text').getall()
      ]
    }

    return news_data_dict


def scrape_novidades(html_content):
    selector = Selector(text=html_content)

    news_links_list = selector.css(
        '.tec--list .tec--card__title__link::attr(href)'
    ).getall()
    return news_links_list


def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)

    next_news_page_link = selector.css('.tec--btn::attr(href)').get()
    return next_news_page_link


def get_tech_news(amount):
    pages_to_scrape = math.ceil(amount/20)
    url = 'https://www.tecmundo.com.br/novidades'
    news_list = []

    for _ in range(pages_to_scrape):
        page = fetch(url)
        news_links = scrape_novidades(page)

        for link in news_links:
            news_page = fetch(link)
            scraped_news = scrape_noticia(news_page)
            news_list.append(scraped_news)
            if len(news_list) == amount:
                break

        url = scrape_next_page_link(page)

    create_news(news_list)
    return news_list
