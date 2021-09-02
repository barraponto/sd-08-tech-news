import requests
import time
from parsel import Selector
import re
import json
from bs4 import BeautifulSoup


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


# Requisito 2
def scrape_noticia(html_content):
    selector = Selector(html_content)
    title = selector.css("h1::text").get()
    url = selector.css('head > link:nth-child(26)::attr(href)').get()
    timestamp = selector.css('#js-article-date::attr(datetime)').get()
    writer = selector.xpath(
        '//*[@id="js-author-bar"]/div/p[1]/a/text()'
        ).get(default=None)
    shares_count = selector.css(
        '#js-author-bar > nav > div:nth-child(1)::text'
        ).get(default='0').strip()
    comments_count = selector.css(
        '#js-comments-btn::attr(data-count)'
        ).get(default='0')
    summary = selector.xpath(
        '//*[@id="js-main"]/div[1]/article/div[3]/div[2]/p[1]/'
        'descendant-or-self::*/text()'
        ).getall()
    r_sources = selector.xpath(
        '//*[@id="js-main"]/div[1]/article/div[3]/div[4]/div/a/text()'
        ).getall()
    sources = remove_spaces(r_sources)
    r_categories = selector.xpath('//*[@id="js-categories"]/a/text()').getall()
    categories = remove_spaces(r_categories)
    dit = {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer.strip(),
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
    """Seu código deve vir aqui"""
