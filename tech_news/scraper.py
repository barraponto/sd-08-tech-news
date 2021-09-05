from parsel import Selector
from math import ceil
import time
import requests
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    try:
        time.sleep(1)
        page = requests.get(url, timeout=3)
        return page.text if page.status_code == 200 else None
    except requests.Timeout:
        return None


# Requisito 2
def find_url(html_content):
    selector = Selector(text=html_content)
    url = selector.xpath('//link[contains(@rel, "canonical")]/@href').get()
    return url


def summary_serializer(summary):
    summary_selector = Selector(text=str(summary))
    summary_list = summary_selector.css("p ::text").getall()
    summary = [summary.replace('\\xa0', '\xa0') for summary in summary_list]
    summary_text = "".join(summary[1:])
    return summary_text


def remove_white_spaces(array):
    newArray = []
    for item in array:
        newArray.append(item[1:-1])
    return newArray


def scrape_noticia(html_content):
    selector = Selector(text=html_content)
    url = find_url(html_content)
    dt = selector.css("div.tec--timestamp--lg div time::attr(datetime)").get()
    shares_text = selector.css("div.tec--toolbar__item::text").get()
    shares = shares_text.split(' ')[1] if shares_text is not None else 0
    com = selector.xpath('//button[@id="js-comments-btn"]/@data-count').get()
    summary = selector.css("div.tec--article__body p").get(),
    str_summary = summary_serializer(summary)
    sources = selector.css("div.z--mb-16 div a::text").getall()
    categories = selector.css("#js-categories a::text").getall()
    writer = selector.css(".z--font-bold a::text").get()\
        or selector.css("p.z--font-bold::text").get()

    info_news = {
        "url": url,
        "title": selector.css("#js-article-title::text").get(),
        "timestamp": dt,
        "writer": writer[1:-1] if writer[0] == ' ' else writer,
        "shares_count": int(shares) if shares != '' else 0,
        "comments_count": int(com) if com != '' else 0,
        "summary": str(str_summary),
        "sources": remove_white_spaces(sources),
        "categories": remove_white_spaces(categories),
    }
    return info_news


# Requisito 3
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    article = "article.tec--card--medium"
    link = "a.tec--card__thumb__link::attr(href)"
    links = selector.css(article + ' ' + link).getall()
    return links if len(links) != 0 else []


# Requisito 4
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    next_page = selector.css("a.tec--btn--lg::attr(href)").get()
    return next_page


# Requisito 5
def get_tech_news(amount):
    full_size = amount
    html_content = fetch("https://www.tecmundo.com.br/novidades")
    news_links = scrape_novidades(html_content)
    data = []
    for _ in range(ceil(amount / 20)):
        size = 20 if full_size >= 20 else full_size - 20
        for link in news_links[:size]:
            page = fetch(link)
            content = scrape_noticia(page)
            data.append(content)
        full_size -= 20
        next_page_link = scrape_next_page_link(html_content)
        next_page = fetch(next_page_link)
        news_links = scrape_novidades(next_page)
    create_news(data)
    return data
