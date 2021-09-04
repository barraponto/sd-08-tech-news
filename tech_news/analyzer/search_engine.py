import re
from datetime import datetime
from tech_news.database import search_news, find_news


def get_result_list(list_to_format):
    """Formats result list for search functions"""
    news_tuple_list = []
    for news in list_to_format:
        title_url_tuple = (news["title"], news["url"])
        news_tuple_list.append(title_url_tuple)
    return news_tuple_list


# Requisito 6
def search_by_title(title):
    """Seu código deve vir aqui"""
    query = re.compile(f"{title}", re.IGNORECASE)
    news_by_title = search_news({"title": query})
    return get_result_list(news_by_title)


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""
    try:
        datetime.strptime(date, "%Y-%m-%d").strftime('%Y-%m-%d')
    except ValueError:
        raise ValueError("Data inválida")
    news_list = find_news()
    news_by_date = []
    for news in news_list:
        if str(news["timestamp"]).startswith(date):
            news_by_date.append(news)
    return get_result_list(news_by_date)


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""
    source_query = re.compile(f"{source}", re.IGNORECASE)
    news_by_source = search_news({"sources": source_query})
    return get_result_list(news_by_source)


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
