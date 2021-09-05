from tech_news.database import search_news
from datetime import datetime


# Requisito 6
def search_by_title(title):
    news = search_news({"title": {"$regex": title, "$options": "si"}})
    result = []
    for item in news:
        tuple_item = (item["title"], item["url"])
        result.append(tuple_item)
    return result


# Requisito 7
def search_by_date(date):
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Data inválida")
    else:
        news = search_news({"timestamp": {"$regex": date}})
        result = []
        for item in news:
            tuple_item = (item["title"], item["url"])
            result.append(tuple_item)
        return result


# Requisito 8
def search_by_source(source):
    news = search_news({"sources": {"$regex": source, "$options": "si"}})
    result = []
    for item in news:
        tuple_item = (item["title"], item["url"])
        result.append(tuple_item)
    return result


# Requisito 9
def search_by_category(category):
    news = search_news({"categories": {"$regex": category, "$options": "si"}})
    result = []
    for item in news:
        tuple_item = (item["title"], item["url"])
        result.append(tuple_item)
    return result
