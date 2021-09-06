import requests
import time
from parsel import Selector


from tech_news.utils.scrape_helper import (
    scrape_news_writer, scrape_news_shares_count
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
      'comments_count': int(
          selector.css('#js-comments-btn::attr(data-count)').get()
      ),
      'summary': ''.join(
          selector.css('.tec--article__body p:first-child *::text').getall()
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


# Requisito 3
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
