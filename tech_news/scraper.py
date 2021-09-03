import requests
import time

from parsel import Selector


# Requisito 1
def fetch(url):
    time.sleep(1)
    try:
        response = requests.get(url, timeout=3)
        status = response.status_code
        if status != 200:
            return None
        return response.text
    except requests.Timeout:
        return None


# Requisito 2
def scrape_noticia(html_content):
    selector = Selector(text=html_content)
    str_url = "head link[rel=canonical]::attr(href)"
    url = selector.css(str_url).get()
    str_title = "#js-article-title::text"
    title = selector.css(str_title).get()
    str_timestamp = "#js-article-date::attr(datetime)"
    timestamp = selector.css(str_timestamp).get()
    str_writer = "p.z--font-bold a::text"
    writer = selector.css(str_writer).get()
    str_shares = "nav.tec--toolbar button.tec--btn"
    shares_count = selector.css(str_shares).re_first(r'\d+')
    str_comments = "#js-comments-btn::attr(data-count)"
    comments_count = selector.css(str_comments).get()
    str_summary = "div.tec--article__body p:first-child *::text"
    summary = selector.css(str_summary).getall()
    summary_formated = []
    for element in summary:
        summary_formated.append(element.strip())
    str_sources = "div div.z--mb-16 div a::text"
    sources = selector.css(str_sources).getall()
    sources_formated = []
    for element in sources:
        sources_formated.append(element.strip())
    str_categories = "div div a.tec--badge.tec--badge--primary::text"
    categories = selector.css(str_categories).getall()
    categories_formated = []
    for element in categories:
        categories_formated.append(element.strip())

    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer.strip(),
        "shares_count": int(shares_count),
        "comments_count": int(comments_count),
        "summary": ' '.join(summary_formated),
        "sources": sources_formated,
        "categories": categories_formated,
    }


# Requisito 3
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    str_novidades = "div h3 a::attr(href)"
    return selector.css(str_novidades).getall()


# Requisito 4
def scrape_next_page_link(html_content):
    try:
        selector = Selector(text=html_content)
        next_1 = "#js-main > div > div > div.z--col.z--w-2-3 > "
        next_2 = "div.tec--list.tec--list--lg > a::attr(href)"
        str_next_page = next_1 + next_2
        return selector.css(str_next_page).get()
    except ValueError:
        return None


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
