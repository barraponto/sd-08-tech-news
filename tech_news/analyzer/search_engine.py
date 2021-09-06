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
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
