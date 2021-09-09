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

    is_none = None

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

    if not writer_selector:
        writer_selector = Selector(text=html_content).css(
            '#js-main > div > article > div.tec--article__body-grid >'
            'div.z--pt-40.z--pb-24 > div.z--flex.z--items-center >'
            'div.tec--timestamp.tec--timestamp--lg >'
            'div.tec--timestamp__item.z--font-bold > a::text').get()

    if not writer_selector:
        writer_selector = Selector(text=html_content).css(
            '#js-author-bar > div >'
            'p.z--m-none.z--truncate.z--font-bold::text').get()

    if writer_selector == is_none:
        news_dict['writer'] = ''
    else:
        news_dict['writer'] = writer_selector.strip()

    shares_count_selector = Selector(text=html_content).css(
        '#js-author-bar > nav > div::text').get()
    if shares_count_selector == is_none:
        news_dict['shares_count'] = 0
    else:
        news_dict['shares_count'] = int(
            ''.join(filter(str.isdigit, shares_count_selector)))

    comments_count_selector = Selector(text=html_content).css(
        '#js-comments-btn::attr(data-count)').get()
    if comments_count_selector == is_none:
        news_dict['comments_count'] = ''
    else:
        news_dict['comments_count'] = int(comments_count_selector)

    summary_selector = Selector(text=html_content).css(
        '.tec--article__body > p:first-of-type *::text').getall()

    # print('antes do IF', summary_selector)
    # if len(summary_selector) == 0:
    #     summary_selector = Selector(text=html_content).css(
    #         '#js-main > div > article > div.tec--article__body-grid >'
    #         'div.tec--article__body.p402_premium >'
    #         'p:nth-child(1) *::text').getall()

    # print('depois do IF', summary_selector)
    summary = [summary for summary in summary_selector]
    # print(summary)
    news_dict['summary'] = ''.join(summary)

    sources_selector = Selector(text=html_content).css(
        "[class='tec--badge']::text").getall()
    sources = [source.strip() for source in sources_selector]
    news_dict['sources'] = sources

    categories_selector = Selector(text=html_content).css(
        '#js-categories > a::text').getall()

    if not categories_selector:
        categories_selector = Selector(text=html_content).css(
            '#js-categories > a:nth-child::text').getall()
    categories = [categorie.strip() for categorie in categories_selector]
    print(categories_selector)
    news_dict['categories'] = categories
    # print(news_dict)
    return news_dict


news_page = 'https://www.tecmundo.com.br/minha-serie/215330-8-series-parecidas-the-crown-fas-realeza.htm'
scrape_noticia(fetch(news_page))


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
    # print(next_page_selector)
    return next_page_selector


# scrape_next_page_link(fetch('https://www.tecmundo.com.br/novidades'))


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    page = 'https://www.tecmundo.com.br/novidades'
    list_news = []
    scrape_novi = scrape_novidades(fetch(page))
    # print(len(list_news))
    # count_news = len(scrape_novi)
    # print(scrape_novi)
    # print(len(scrape_novi))
    while amount >= len(list_news):
        for each_news in scrape_novi:
            list_news.append(scrape_noticia(fetch(each_news)))
            # print(list_news)
            # print(len(list_news))
            # print(page)
            if amount == len(list_news):
                create_news(list_news)
                return list_news
        page = scrape_next_page_link(fetch(page))


# get_tech_news(41)
