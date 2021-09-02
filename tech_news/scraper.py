import requests
from time import sleep
from parsel import Selector
from requests.exceptions import Timeout


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
    url = selector.css("link").xpath("./@href").extract()[-2]
    title = (
        selector.css(".tec--article__header__title").xpath("//h1/text()").get()
    )
    timestamp = selector.css("time").xpath("@datetime").get()
    writer = (
        selector.css(".tec--author__info__link").xpath("text()").get().strip()
        or None
    )
    # || None
    shares_count = (
        int(
            selector.css(".tec--toolbar__item")
            .xpath("text()")
            .get()
            .split()[0]
        )
        or 0
    )
    # || 0
    comments_count = (
        int(
            selector.css(".tec--toolbar__item")[1]
            .xpath("//button/text()")
            .getall()[1]
            .split()[0]
        )
        or 0
    )
    summary = "".join(selector.xpath("//p")[2].css("*::text").getall())
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
    return result


# Requisito 3
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
