import tech_news.database as db
from datetime import datetime


# Requisito 6
def search_by_title(title):
    """Seu código deve vir aqui"""
    found_news = db.find_news()
    return [
        (new["title"], new["url"])
        for new in found_news
        if title.lower() in new["title"].lower()
    ]


# Requisito 7
def validate_date(date):
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Data inválida")


def search_by_date(date):
    """Seu código deve vir aqui"""
    validate_date(date)
    found_news = db.find_news()
    return [
        (new["title"], new["url"])
        for new in found_news
        if datetime.strptime(date, "%Y-%m-%d").date()
        == datetime.strptime(new["timestamp"], "%Y-%m-%dT%H:%M:%S").date()
    ]


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""
    found_news = db.find_news()
    return [
        (new["title"], new["url"])
        for new in found_news
        if source.lower()
        in (post_source.lower() for post_source in new["sources"])
    ]


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
    found_news = db.find_news()
    return [
        (new["title"], new["url"])
        for new in found_news
        if category.lower()
        in (post_category.lower() for post_category in new["categories"])
    ]
