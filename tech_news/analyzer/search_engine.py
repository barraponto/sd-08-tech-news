import re
import datetime
from tech_news.database import search_news


def serialize_news_list(news_list):
    result = []
    for news in news_list:
        result.append((news["title"], news["url"]))
    return result


# Requisito 6
def search_by_title(title):
    """Seu código deve vir aqui"""
    news_list = search_news({"title": re.compile(title, re.IGNORECASE)})
    if not news_list:
        return []

    return serialize_news_list(news_list)


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""
    try:
        datetime.datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Data inválida")

    news_list = search_news({"timestamp": re.compile(date)})
    if not news_list:
        return []

    return serialize_news_list(news_list)


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""
    news_list = search_news({"sources": re.compile(source, re.IGNORECASE)})
    if not news_list:
        return []

    return serialize_news_list(news_list)


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
