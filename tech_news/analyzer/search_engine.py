import re
import datetime
from tech_news.database import search_news


def get_result_list(list_to_format):
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
    year, month, day = date.split('-')
    date_query = datetime.date(int(year), int(month), int(day))
    news_by_date = search_news({"timestamp": date_query})
    return get_result_list(news_by_date)


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
