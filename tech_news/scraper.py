import requests
import time
import re
from parsel import Selector


# Requisito 1
def fetch(url):
    time.sleep(1)

    try:
        response = requests.get(url, timeout=3)
    except requests.ReadTimeout:
        return None

    if response.status_code == 200:
        return response.text
    else:
        return None


# Requisito 2
def scrape_noticia(html_content):
    selector = Selector(html_content)
    news_info = {}

    xpath_queries = [
        ("url", "//head/link[@rel='canonical']/@href"),
        ("title", "//h1[@id='js-article-title']/text()"),
        ("timestamp", "//time[@id='js-article-date']/@datetime"),
        ("writer", "//a[@class='tec--author__info__link']/text()"),
        ("shares_count", "//div[@class='tec--toolbar__item'][1]/text()"),
        ("comments_count", "//button[@id='js-comments-btn']/text()[2]"),
        (
            "summary",
            (
                "//div[@class='tec--article__body z--px-16 p402_premium']"
                "/p[1]/descendant-or-self::*/text()"
            ),
        ),
        ("sources", "//h2[text()='Fontes']/following-sibling::div/a/text()"),
        ("categories", "//div[@id='js-categories']/a/text()"),
    ]

    for element in xpath_queries:
        query_result = selector.xpath(element[1]).getall()
        is_list = element[0] in ("sources", "categories")

        query_result = (
            query_result[0].strip()
            if len(query_result) == 1 and not is_list
            else query_result
        )

        if "count" in element[0]:
            query_result = int(re.sub(r"\D", "", query_result)) or 0

        if element[0] == "summary":
            query_result = "".join(query_result)

        if is_list:
            query_result = [x.strip() for x in query_result]

        news_info[element[0]] = query_result

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
    """Seu código deve vir aqui"""
