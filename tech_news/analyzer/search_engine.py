from tech_news.database import search_news
from datetime import datetime


# Requisito 6
def search_by_title(title):
    query = {"title": {"$regex": title, "$options": "i"}}
    # https://docs.mongodb.com/manual/reference/operator/query/regex/
    return [(info["title"], info["url"]) for info in search_news(query)]


# Requisito 7
def search_by_date(date):
    query = {"timestamp": {"$regex": date}}
    try:
        datetime.strptime(date, "%Y-%m-%d")
        # https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes
    except ValueError:
        raise ValueError("Data inválida")
    return[(info["title"], info["url"]) for info in search_news(query)]


# Requisito 8
def search_by_source(source):
    query = {"sources": {"$regex": source, "$options": "i"}}
    return [(info["title"], info["url"]) for info in search_news(query)]


# Requisito 9
def search_by_category(category):
    query = {"categories": {"$regex": category, "$options": "i"}}
    return [(info["title"], info["url"]) for info in search_news(query)]
