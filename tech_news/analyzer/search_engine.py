from tech_news.database import search_news
from datetime import datetime


# Requisito 6
def search_by_title(title):
    """Seu código deve vir aqui"""
    news = search_news({"title": {"$regex": title, "$options": "i"}})
    result = []
    if len(news) > 0:
        for news in news:
            result.append((news["title"], news["url"]))
        return result
    else:
        return []


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""
    try:
        datetime.strptime(date, "%Y-%m-%d")
        news = search_news({"timestamp": {"$regex": date}})
        result = []
        if len(news) > 0:
            for news in news:
                result.append((news["title"], news["url"]))
            return result
        else:
            return []
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""
    news = search_news({"sources": {"$regex": source, "$options": "i"}})
    result = []
    if len(news) > 0:
        for news in news:
            result.append((news["title"], news["url"]))
        return result
    else:
        return []


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
    news = search_news({"categories": {"$regex": category, "$options": "i"}})
    result = []
    if len(news) > 0:
        for news in news:
            result.append((news["title"], news["url"]))
        return result
    else:
        return []