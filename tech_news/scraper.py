import requests
import time
from parsel import Selector
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    """Seu código deve vir aqui"""
    try:
        response = requests.get(url, timeout=3)
        time.sleep(1)
        if(response.status_code != 200):
            return None
        return response.text
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    url = selector.css("head [rel='canonical'] ").css("link::attr(href)").get()
    title_content = selector.css("h1::text").get()
    timestamp = selector.css("time::attr(datetime)").get()
    writer = selector.css("a.tec--author__info__link::text").get()
    if writer is not None:
        writer = writer.strip()
    shares = selector.css("div.tec--toolbar__item::text").get()
    if shares is None:
        shares = 0
    else:
        shares = str(shares).split()[0]
    coment = selector.css(".tec--toolbar__item button::attr(data-count)").get()

    summary = selector.css("div.tec--article__body p:first-child *::text")
    summary_content = summary.getall()
    summary_join = "".join(str(item) for item in summary_content)

    sources_content = selector.css("div.z--mb-16 a.tec--badge::text").getall()
    sources = []
    for item in sources_content:
        sources.append(item.strip())

    categories_content = selector.css("a.tec--badge--primary::text").getall()
    categories = []
    for item in categories_content:
        categories.append(item.strip())

    new_dict = {
        "url": url,
        "title": title_content,
        "timestamp": timestamp,
        "writer": writer,
        "shares_count": int(shares),
        "comments_count": int(coment),
        "summary": summary_join,
        "sources": sources,
        "categories": categories
    }

    return(new_dict)


# Requisito 3
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    links = selector.css("h3.tec--card__title a::attr(href)").getall()
    return links


# Requisito 4
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    loadMore = selector.css(".tec--btn--primary::attr(href)").get()
    return loadMore


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    url_fetch = "https://www.tecmundo.com.br/novidades"
    loops = (amount // 20.1) + 1
    list_links = []
    count_loops = 0
    list_dict_news = []

    while count_loops < loops:
        html_content = fetch(url_fetch)
        page_links_scraped = scrape_novidades(html_content)
        url_fetch = scrape_next_page_link(html_content)
        count_loops += 1
        for link in page_links_scraped:
            if len(list_links) < amount:
                list_links.append(link)

    for link in list_links:
        html_content = fetch(link)
        dict_news = scrape_noticia(html_content)
        list_dict_news.append(dict_news)

    create_news(list_dict_news)

    return list_dict_news
