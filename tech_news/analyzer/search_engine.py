import tech_news.database as db
from datetime import datetime


# Requisito 6
def search_by_title(title):
    find_tech_news = db.find_news()
    result = [
        (tech_news["title"], tech_news["url"])
        for tech_news in find_tech_news
        if title.lower() in tech_news["title"].lower()
    ]
    return result


# Requisito 7
def search_by_date(date):
    find_tech_news = db.find_news()
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Data inválida")
    result = [
        (tech_news["title"], tech_news["url"])
        for tech_news in find_tech_news
        if datetime.strptime(date, "%Y-%m-%d").date()
        == datetime.strptime(
            tech_news["timestamp"], "%Y-%m-%dT%H:%M:%S"
        ).date()
    ]
    return result


# Requisito 8
def search_by_source(source):
    find_tech_news = db.find_news()
    result = [
        (tech_news["title"], tech_news["url"])
        for tech_news in find_tech_news
        if source.lower()
        in (tech_source.lower() for tech_source in tech_news["sources"])
    ]
    return result


# Requisito 9
def search_by_category(category):
    find_tech_news = db.find_news()
    result = [
        (tech_news["title"], tech_news["url"])
        for tech_news in find_tech_news
        if category.lower()
        in (tech_category.lower() for tech_category in tech_news["categories"])
    ]
    return result
