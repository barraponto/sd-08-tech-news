import tech_news.database as db
from datetime import datetime


# Requisito 6
def search_by_title(title):
    """Seu código deve vir aqui"""
    news = db.find_news()
    news_list = []
    for item in news:
        if item["title"].lower() == title.lower():
            content = (item["title"], item["url"])
            news_list.append(content)
    return news_list


# Requisito 7
def search_by_date(date):
    news = db.find_news()
    try:
        news_list = []
        for item in news:
            if datetime.strptime(date, "%Y-%m-%d").date() == datetime.strptime(
                item["timestamp"], "%Y-%m-%dT%H:%M:%S"
            ).date():
                content = (item["title"], item["url"])
                news_list.append(content)
        return news_list
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""
    news = db.find_news()
    news_list = []
    for item in news:
        for src in item["sources"]:
            if src.lower() == source.lower():
                content = (item["title"], item["url"])
                news_list.append(content)
    return news_list


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
