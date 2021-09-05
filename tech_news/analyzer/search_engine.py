from tech_news.database import search_news
from datetime import datetime


# Requisito 6
def search_by_title(title):
    news = search_news({"title": {"$regex": title, "$options": "si"}})
    searchResults = list()

    for item in news:
        searchResults.append((item["title"], item["url"]))

    return searchResults


# Requisito 7
def search_by_date(date):
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Data inválida")
    else:
        news = search_news({"timestamp": {"$regex": date}})
        searchResults = list()

        for item in news:
            searchResults.append((item["title"], item["url"]))

        return searchResults


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
