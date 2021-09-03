import requests
from time import sleep
from parsel import Selector
from requests.exceptions import Timeout
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    sleep(1)
    try:
        response = requests.get(
            url, timeout=3, headers={"Accept": "application/json"}
        )
    except Timeout:
        return None
    if response.status_code != 200:
        return None
    return response.text


# Requisito 2
def scrape_noticia(html_content):
    selector = Selector(text=html_content)
    url = selector.css("link[rel=canonical]::attr(href)").get() or None
    title = (
        selector.css(".tec--article__header__title").xpath("//h1/text()").get()
        or None
    )
    timestamp = selector.css("time").xpath("@datetime").get() or None
    writer = ""
    writer1 = selector.css(".tec--author__info__link").xpath("text()").get()
    writer2 = selector.css("a[href*=autor]").xpath("text()").get()
    if writer1:
        writer = writer1.strip()
    elif writer2:
        writer = writer2
    else:
        writer = None
    shares_count = int(selector.css(".tec--btn::attr(data-count)").get() or 0)
    comments_count = 0
    if len(selector.css(".tec--toolbar__item")) > 1:
        comments_count = (
            int(
                selector.css(".tec--toolbar__item")[1]
                .xpath("//button/text()")
                .getall()[1]
                .split()[0]
            )
            or 0
        )
    summary = "".join(
        selector.css(".tec--article__body > p:first-child")
        .css("*::text")
        .getall()
    )
    len_badge = len(selector.css(".tec--badge").xpath("text()").getall())
    len_primary = len(
        selector.css(".tec--badge--primary").xpath("text()").getall()
    )
    sources_not_striped = (
        selector.css(".tec--badge")
        .xpath("text()")
        .getall()[: (len_badge - len_primary)]
    )
    sources = [item.strip() for item in sources_not_striped]
    categories_not_striped = (
        selector.css(".tec--badge--primary").xpath("text()").getall()
    )
    categories = [item.strip() for item in categories_not_striped]
    result = {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "shares_count": shares_count,
        "comments_count": comments_count,
        "summary": summary,
        "sources": sources,
        "categories": categories,
    }
    if not result:
        result = {
            "url": None,
            "title": None,
            "timestamp": None,
            "writer": None,
            "shares_count": 0,
            "comments_count": 0,
            "summary": None,
            "sources": [],
            "categories": [],
        }
    return result


# Requisito 3
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    list_links = (
        selector.css(".tec--main")
        .css(".tec--card__title__link")
        .xpath("./@href")
        .getall()
    )
    return list_links


# Requisito 4
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    link_next = selector.css(".tec--btn--lg").xpath("./@href").get() or None
    return link_next


# Requisito 5
def get_tech_news(amount):
    # print(amount)
    page_n = fetch("https://www.tecmundo.com.br/novidades")
    # print("https://www.tecmundo.com.br/novidades")
    index = 0
    result_info = []
    while amount > 0:
        if index > 19:
            print(scrape_next_page_link(page_n))
            page_n = fetch(scrape_next_page_link(page_n))
            index = 0
        list_news = scrape_novidades(page_n)
        read_news = scrape_noticia(fetch(list_news[index]))
        result_info.append(read_news)
        # print(list_news[index])
        # print(index, amount)
        index += 1
        amount -= 1
    create_news(result_info)
