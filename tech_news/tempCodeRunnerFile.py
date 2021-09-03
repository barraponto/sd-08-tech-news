import requests
import time
from parsel import Selector


url = 'https://www.tecmundo.com.br/'
news = 'mobilidade-urbana-smart-cities/155000-musk-tesla-carros-totalmente-autonomos.htm'
news_page = url + news


# Requisito 1
def fetch(url):
    """Seu código deve vir aqui"""
    try:
        response = requests.get(url, timeout=3)
        time.sleep(1)
        # print(response.text)
        # print(response.status_code)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""
    # print(html_content)
    news_dict = {
        'url': '',
        'title': '',
        'timestamp': '',
        'writer': '',
        'shares_count': '',
        'comments_count': '',
        'summary': '',
        'sources': [],
        'categories': [],
    }

    url_selector = Selector(text=html_content).css(
        'head >link:nth-child(26)::attr(href)').get()
    news_dict['url'] = url_selector

    title_selector = Selector(text=html_content).css(
        '#js-article-title *::text').get()
    news_dict['title'] = title_selector

    timestamp_selector = Selector(text=html_content).css(
        '#js-article-date::attr(datetime)').get()
    news_dict['timestamp'] = timestamp_selector

    writer_selector = Selector(text=html_content).css(
        '#js-author-bar > div > p.z--m-none.z--truncate.z--font-bold >'
        'a::text').get()
    news_dict['writer'] = writer_selector.strip()

    shares_count_selector = Selector(text=html_content).css(
        '#js-author-bar > nav > div::text').get()
    news_dict['shares_count'] = int(
        ''.join(filter(str.isdigit, shares_count_selector)))

    comments_count_selector = Selector(text=html_content).css(
        '#js-comments-btn::attr(data-count)').get()
    news_dict['comments_count'] = int(comments_count_selector)

    summary_selector = Selector(text=html_content).css(
        '#js-main > div.z--container > article > div.tec--article__body-grid >'
        'div.tec--article__body.z--px-16.p402_premium >'
        'p:nth-child(1) *::text').getall()
    # print(summary_selector)
    summary = [summary.strip() for summary in summary_selector]
    # print(summary)
    news_dict['summary'] = ' '.join(summary)

    sources_selector = Selector(text=html_content).css(
        '#js-main > div.z--container > article > div.tec--article__body-grid >'
        'div.z--mb-16.z--px-16 > div > a::text').getall()
    sources = [source.strip() for source in sources_selector]
    news_dict['sources'] = sources

    categories_selector = Selector(text=html_content).css(
        '#js-categories > a::text').getall()
    categories = [categorie.strip() for categorie in categories_selector]
    # print(categories_selector)
    news_dict['categories'] = categories
    # print(news_dict)
    return news_dict


# scrape_noticia(fetch(news_page))


# Requisito 3
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""
    urls_news_selector = Selector(text=html_content).css(
        '#js-main > div > div > div.z--col.z--w-2-3 >'
        'div.tec--list.tec--list--lg > div > article >'
        'div > h3 > a::attr(href)').getall()
    # print(urls_news_selector)
    return urls_news_selector


# scrape_novidades(fetch('https://www.tecmundo.com.br/novidades'))


# Requisito 4
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    next_page_selector = Selector(text=html_content).css(
        '#js-main > div > div > div.z--col.z--w-2-3 >'
        'div.tec--list.tec--list--lg > a::attr(href)').get()
    print(next_page_selector)
    return next_page_selector


scrape_next_page_link(fetch('https://www.tecmundo.com.br/novidades'))