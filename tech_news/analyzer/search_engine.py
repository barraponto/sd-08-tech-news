from tech_news.database import search_news
from datetime import datetime


# Requisito 6
def search_by_title(title):
    news = search_news({"title": {"$regex": title, "$options": "i"}})
    print(news)
    return [(actual_news["title"], actual_news["url"]) for actual_news in news]


def date_is_valid(date):
    try:
        datetime.strptime(date, "%Y-%m-%d")
        return True
    except ValueError:
        return False


# Requisito 7
def search_by_date(date):
    try:
        datetime.strptime(date, "%Y-%m-%d")
        news = search_news({"timestamp": {"$regex": date, "$options": "i"}})
        return [
            (actual_news["title"], actual_news["url"]) for actual_news in news
        ]
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_source(source):
    news = search_news({"sources": {"$regex": source, "$options": "i"}})
    return [(actual_news["title"], actual_news["url"]) for actual_news in news]


# Requisito 9
def search_by_category(category):
    news = search_news({"categories": {"$regex": category, "$options": "i"}})
    return [(actual_news["title"], actual_news["url"]) for actual_news in news]
