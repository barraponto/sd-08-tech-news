import requests
import time
from parsel import Selector
import re
import json
from bs4 import BeautifulSoup
from tech_news.database import create_news


def fetch(url):
    try:
        response = requests.get(url, timeout=3)
        time.sleep(1)
        if response.status_code != 200:
            return None
        return response.text
    except requests.Timeout:
        return None


def remove_spaces(text):
    result = []
    for i in text:
        j = i.strip()
        result.append(j)
    return result


def get_writer(selector):
    writer_top = selector.css(".tec--author__info__link").xpath("text()").get()
    writer_mid = selector.css("a[href*=autor]").xpath("text()").get()
    writer_bot = selector.css(".tec--author__info> p::text").get()
    if writer_top:
        return writer_top.strip()
    elif writer_mid:
        return writer_mid.strip()
    elif writer_bot:
        return writer_bot
    return None


# Requisito 2
def scrape_noticia(html_content):
    selector = Selector(html_content)
    title = selector.css("h1::text").get()
    url = selector.css('head > link:nth-child(26)::attr(href)').get()
    timestamp = selector.css('#js-article-date::attr(datetime)').get()
    writer = get_writer(selector)
    shares_count = selector.css(
        '#js-author-bar > nav > div:nth-child(1)::text'
        ).get(default='0').strip()
    comments_count = selector.css(
        '#js-comments-btn::attr(data-count)'
        ).get(default='0')
    summary = selector.css(
        '.tec--article__body > p:first-child').xpath(
            'descendant-or-self::*/text()').getall()
    len_source = len(selector.css(".tec--badge::text").getall())
    len_categories = len(
        selector.css(".tec--badge--primary::text").getall()
    )
    r_sources = selector.css(
        ".tec--badge::text").getall()[: len_source - len_categories]
    sources = remove_spaces(r_sources)
    r_categories = selector.xpath('//*[@id="js-categories"]/a/text()').getall()
    categories = remove_spaces(r_categories)
    dit = {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "shares_count": int(re.search(r'\d+', shares_count).group()),
        "comments_count": int(comments_count),
        "summary": ''.join(summary),
        "sources": sources,
        "categories": categories,
    }
    return dit


# Requisito 3
def scrape_novidades(html_content):
    if html_content == "":
        return []
    selector = Selector(html_content)
    urls = selector.css("body > script:nth-child(6)").get()
    soup = BeautifulSoup(urls, 'html.parser')
    res = soup.find('script')
    json_object = json.loads(res.contents[0])
    array_urls = []
    for item in json_object['itemListElement']:
        array_urls.append(item['url'])
    return array_urls


# Requisito 4
def scrape_next_page_link(html_content):
    if html_content == "":
        return None
    selector = Selector(html_content)
    urls = selector.xpath(
        '//*[@id="js-main"]/div/div/div[1]/div[2]/a/@href'
        ).get()
    return urls


# Requisito 5
def get_tech_news(amount):
    page = fetch("https://www.tecmundo.com.br/novidades")
    index = 0
    result = []
    novidades = scrape_novidades(page)
    count_news = len(novidades)
    while amount > 0:
        if index >= count_news:
            index = 0
            page = fetch(scrape_next_page_link(page))
            novidades = scrape_novidades(page)
        dit_news = scrape_noticia(fetch(novidades[index]))
        result.append(dit_news)
        index += 1
        amount-= 1
    create_news(result)
    return result
