# 1 - CSS arttribute selector:
# https://developer.mozilla.org/en-US/docs/Web/CSS/Attribute_selectors
# 2 - CSS first of type selector:
# https://www.w3schools.com/cssref/sel_first-of-type.asp
from requests import get
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    time.sleep(1)
    try:
        response = get(url, headers={"Accept": "text/html"}, timeout=3)
    except Exception:
        return None

    if response.status_code == 200:
        return response.text
    return None


# Requisito 2
def scrape_noticia(html_content):
    selector = Selector(text=html_content)
    print('SELECTOR', selector)
    url = selector.css("head link[rel=canonical]::attr(href)").get()  # 1
    title = selector.css(".tec--article__header__title::text").get()
    timestamp = selector.css("#js-article-date::attr(datetime)").get()
    writer = selector.css(".tec--author__info__link::text").get()
    share_count = selector.css(".tec--toolbar__item::text").get().split(" ")[1]
    comments_count = selector.css("#js-comments-btn::attr(data-count)").get()
    summary = ''.join(selector.css(
        ".tec--article__body p:first-of-type *::text"
    ).getall())  # 2
    sources = selector.css("[class='tec--badge']::text").getall()
    mapped_sources = [i.strip() for i in sources]
    categories = selector.css("#js-categories a::text").getall()
    mapped_categories = [i.strip() for i in categories]
    response_dict = {
        'url': url,
        'title': title,
        'timestamp': timestamp,
        'writer': writer.strip(),
        'shares_count': share_count if share_count != '0' else 0,
        'comments_count': comments_count if comments_count != '0' else 0,
        'summary': summary,
        'sources': mapped_sources,
        'categories': mapped_categories,
    }
    return response_dict


# Requisito 3
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
