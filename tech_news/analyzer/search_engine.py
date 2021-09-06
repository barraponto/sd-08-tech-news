from datetime import datetime
from tech_news.database import search_news


def format_search_result(results):
    return [(result["title"], result["url"]) for result in results]


# Requisito 6
def search_by_title(title):
    results = search_news({"title": {"$regex": title, "$options": "i"}})
    return format_search_result(results)


# Requisito 7
def search_by_date(date):
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Data inválida")
    results = search_news({"timestamp": {"$regex": date}})
    return format_search_result(results)


# Requisito 8
def search_by_source(source):
    regex_source = "^" + source + "$"
    results = search_news({"sources": {"$elemMatch":
                          {"$regex": regex_source, "$options": "i"}}})
    return format_search_result(results)


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
    regex_category = "^" + category + "$"
    results = search_news({"categories": {"$elemMatch":
                          {"$regex": regex_category, "$options": "i"}}})
    return format_search_result(results)
