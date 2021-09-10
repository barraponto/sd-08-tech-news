from tech_news.database import search_news
from datetime import datetime


def array_filter(array):
    return [(array["title"], array["url"]) for array in array]


# Requisito 6
def search_by_title(title):
    news = search_news({"title": {"$regex": title, "$options": "i"}})
    return array_filter(news)


# Requisito 7
def search_by_date(date):
    try:
        datetime.fromisoformat(date)
    except ValueError:
        raise ValueError("Data inválida")
    news = search_news({"timestamp": {"$regex": date, "$options": "i"}})
    return array_filter(news)


# Requisito 8
def search_by_source(source):
    news = search_news({"sources": {"$regex": source, "$options": "i"}})
    return array_filter(news)


# Requisito 9
def search_by_category(category):
    news = search_news({"categories": {"$regex": category, "$options": "i"}})
    return array_filter(news)
