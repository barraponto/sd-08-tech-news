from tech_news.database import search_news
import datetime


# Requisito 6
def search_by_title(title):
    
    news = []
    result = search_news({"title": {"$regex": title, "$options": "i"}})

    for index in result:
        news.append((index["title"], index["url"]))

    return news


# Requisito 7
def search_by_date(date):
    try:
        datetime.datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        raise ValueError("Data inválida")
    
    news = []
    result = search_news({"timestamp": {"$regex": date}})

    for index in result:
        news.append((index["title"], index["url"]))

    return news


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
