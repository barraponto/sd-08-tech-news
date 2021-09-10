import requests
import time
import re
from parsel import Selector
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    time.sleep(1)

    try:
        response = requests.get(url)
    except requests.ReadTimeout:
        return None

    if response.status_code == 200:
        return response.text
    else:
        return None


def multi_fetch(url, tries=10):
    html = None
    counter = tries

    while counter > 0:
        html = fetch(url)
        if html is not None:
            break
        counter -= 1

    return html


# Requisito 2
def data_cleanup(query_result, element):
    result = query_result

    if "count" in element[0]:
        try:
            print(result)
            result = int(re.sub(r"\D", "", "".join(result)))
        except ValueError:
            result = 0

    if element[0] == "summary":
        result = "".join(result)

    return result


def scrape_noticia(html_content):
    selector = Selector(html_content)
    news_info = {}

    xpath_queries = [
        ("url", "//head/link[@rel='canonical']/@href"),
        ("title", "//h1[@id='js-article-title']/text()"),
        ("timestamp", "//time[@id='js-article-date']/@datetime"),
        (
            "writer",
            (
                "(//a["
                "contains(@href,'https://www.tecmundo.com.br/autor/')"
                "and not(contains(., '<img'))]"
                "|"
                "//div[contains(@class, 'tec--author__info')]/p[1])/text()"
            ),
        ),
        (
            "shares_count",
            (
                "//div[contains(@class, 'tec--toolbar__item')"
                "and contains(., 'Compartilharam')]/text()"
            ),
        ),
        ("comments_count", "//button[@id='js-comments-btn']/text()"),
        (
            "summary",
            (
                "//div[contains(@class, 'tec--article__body')]"
                "/p[1]/descendant-or-self::*/text()"
            ),
        ),
        ("sources", "//h2[text()='Fontes']/following-sibling::div/a/text()"),
        ("categories", "//div[@id='js-categories']/a/text()"),
    ]

    for element in xpath_queries:
        query_result = selector.xpath(element[1]).getall()
        is_list = element[0] in ("sources", "categories")

        if not is_list and "count" not in element[0]:
            query_result = (
                query_result[0].strip()
                if len(query_result) == 1
                else "".join(query_result).strip()
            )

        if is_list:
            query_result = [x.strip() for x in query_result]

        news_info[element[0]] = data_cleanup(query_result, element)

    return news_info


# Requisito 3
def scrape_novidades(html_content):
    selector = Selector(html_content)

    xpath_query = (
        "//div[@class='tec--list__item']"
        "//a[@class='tec--card__title__link']/@href"
    )

    all_news = selector.xpath(xpath_query).getall()

    return all_news


# Requisito 4
def scrape_next_page_link(html_content):
    selector = Selector(html_content)

    xpath_query = "//a[text()=' Mostrar mais notícias ']/@href"

    next_page_url = selector.xpath(xpath_query).get()

    return next_page_url


# Requisito 5
def get_tech_news(amount):
    all_urls = []
    all_news = []
    html = fetch("https://www.tecmundo.com.br/novidades")

    while len(all_urls) < amount:
        new_urls = scrape_novidades(html)
        all_urls += new_urls

        if len(all_urls) >= amount:
            break

        html = fetch(scrape_next_page_link(html))

    all_urls = all_urls[:amount]

    for url in all_urls:
        html = fetch(url)
        news_data = scrape_noticia(html)
        all_news.append(news_data)

    create_news(all_news)
    return all_news
