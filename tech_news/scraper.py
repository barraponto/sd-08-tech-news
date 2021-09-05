from parsel import Selector
import time
import requests


# Requisito 1
def fetch(url):
    try:
        time.sleep(1)
        page = requests.get(url, timeout=3)
        return page.text if page.status_code == 200 else None
    except requests.Timeout:
        return None


# Requisito 2
base_url = 'https://www.tecmundo.com.br'
def filter_url(link):
    return base_url in link


def find_url(html_content):
    selector = Selector(text=html_content)
    href_links = selector.css('head link::attr(href)').getall()
    return list(filter(filter_url, href_links))[-1]


def summary_serializer(summary):
    summary_selector = Selector(text=str(summary))
    summary_text = summary_selector.css("p ::text").getall()
    return "".join(summary_text[1:])


def remove_white_spaces(array):
    newArray = []
    for item in array:
        newArray.append(item[1:-1])
    return newArray


def scrape_noticia(html_content):
    selector = Selector(text=html_content)
    url = find_url(html_content)
    shares = selector.css("div.tec--toolbar__item::text").get().split(' ')[1]
    comments = selector.css("#js-comments-btn::text").get().split(' ')[1]
    summary = selector.css("div.tec--article__body p").get(),
    str_summary = summary_serializer(summary)
    sources = selector.css("div.z--mb-16 div a::text").getall()
    categories = selector.css("#js-categories a::text").getall()

    info_news = {
        "url": url,
        "title": selector.css("#js-article-title::text").get(),
        "timestamp": selector.css("div.tec--timestamp--lg div time::attr(datetime)").get(),
        "writer": selector.css(".tec--author__info__link::text").get()[1:-1],
        "shares_count": int(shares) if shares !='' else 0,
        "comments_count": int(comments) if comments !='' else 0,
        "summary": str_summary,
        "sources": remove_white_spaces(sources),
        "categories": remove_white_spaces(categories),
    }
    return info_news


# Requisito 3
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
