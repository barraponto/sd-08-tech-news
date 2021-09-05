import re
from datetime import datetime
from tech_news.database import search_news


def serialize(news_list):
    return [(news["title"], news["url"]) for news in news_list]


# Requisito 6
def search_by_title(title):
    news = search_news({"title": re.compile(title, re.IGNORECASE)})
    return serialize(news)


# Requisito 7
def search_by_date(date):
    try:
        datetime.fromisoformat(date).timestamp()
    except ValueError:
        raise ValueError("Data inválida")

    news = search_news({"timestamp": re.compile(date)})
    return serialize(news)


# Requisito 8
def search_by_source(source):
    news = search_news({"sources": re.compile(source, re.IGNORECASE)})
    return serialize(news)


# Requisito 9
def search_by_category(category):
    news = search_news({"categories": re.compile(category, re.IGNORECASE)})
    return serialize(news)
