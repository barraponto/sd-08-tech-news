import re
from tech_news.database import search_news
from datetime import datetime


def format(news_list):
    return [
        (list["title"], list["url"]) for list in news_list
        ]


# Requisito 6
def search_by_title(title):
    """Seu código deve vir aqui"""
    news = search_news({"title": re.compile(title, re.IGNORECASE)})
    return format(news)


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""
    try:
        datetime.fromisoformat(date).timestamp()
    except ValueError:
        raise ValueError("Data inválida")
    news = search_news({"timestamp": re.compile(date)})
    return format(news)


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
