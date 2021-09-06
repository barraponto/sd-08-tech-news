from datetime import datetime
from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    query = search_news({"title": {"$regex": title, "$options": "i"}})
    search_results = list()

    for item in query:
        search_results.append((item["title"], item["url"]))

    return search_results


# Requisito 7
def search_by_date(date):
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Data inválida")

    query = search_news({"timestamp": {"$regex": date}})
    search_results = list()

    for item in query:
        search_results.append((item["title"], item["url"]))

    return search_results


# Requisito 8
def search_by_source(source):
    query = search_news({"sources": {"$regex": source, "$options": "i"}})
    search_results = list()

    for item in query:
        search_results.append((item["title"], item["url"]))

    return search_results


# Requisito 9
def search_by_category(category):
    query = search_news({"categories": {"$regex": category, "$options": "i"}})
    search_results = list()

    for item in query:
        search_results.append((item["title"], item["url"]))

    return search_results
