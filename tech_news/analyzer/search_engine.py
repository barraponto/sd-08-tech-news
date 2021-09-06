from datetime import datetime
from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    results = search_news({"title": {"$regex": title, "$options": "i"}})
    return [(result["title"], result["url"]) for result in results]


# Requisito 7
def search_by_date(date):
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Data inválida")
    results = search_news({"timestamp": {"$regex": date}})
    return [(result["title"], result["url"]) for result in results]


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
