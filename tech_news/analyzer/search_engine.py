import re
from tech_news.database import search_news
from datetime import datetime


"""Ref: estudante Paulo Simões"""


def serialize(news_list):
    return [(news['title'], news['url']) for news in news_list]


# Requisito 6
def search_by_title(title):
    """From a given string, return news with matching title"""
    news = search_news({'title': re.compile(title, re.IGNORECASE)})
    return serialize(news)


# Requisito 7
def search_by_date(date):
    """From a given date, return matching news"""
    try:
        datetime.fromisoformat(date).timestamp()
    except ValueError:
        raise ValueError('Data inválida')

    news = search_news({'timestamp': re.compile(date)})
    return serialize(news)


# Requisito 8
def search_by_source(source):
    """From a given string, return news witch matching source"""
    news = search_news({'sources': re.compile(source, re.IGNORECASE)})
    return serialize(news)


# Requisito 9
def search_by_category(category):
    """From a given string, return news with matching categories"""
    news = search_news({'categories': re.compile(category, re.IGNORECASE)})
    return serialize(news)
