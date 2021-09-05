import datetime
from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    title_formated = {"title": {"$regex": title, "$options": "i"}}
    search_list = search_news(title_formated)
    return [(new["title"], new["url"]) for new in search_list]


# Requisito 7
def search_by_date(date):
    try:
        datetime.datetime.strptime(date, "%Y-%m-%d")
        timestamp_formated = {"timestamp": {"$regex": date}}
        search_list = search_news(timestamp_formated)
        return [(new["title"], new["url"]) for new in search_list]
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_source(source):
    source_formated = {"sources": {"$regex": source, "$options": "i"}}
    search_list = search_news(source_formated)
    return [(new["title"], new["url"]) for new in search_list]


# Requisito 9
def search_by_category(category):
    category_formated = {"categories": {"$regex": category, "$options": "i"}}
    search_list = search_news(category_formated)
    return [(new["title"], new["url"]) for new in search_list]
