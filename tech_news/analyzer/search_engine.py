from tech_news.database import search_news
from datetime import datetime


# Requisito 6
def search_by_title(title):
    query = {"title": {"$regex": f".*{title}.*", "$options": "i"}}
    news = search_news(query)
    return [(new["title"], new["url"]) for new in news]


# Requisito 7
def date_validate(date):
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        return False


def search_by_date(date):
    if date_validate(date) is False:
        raise ValueError("Data inválida")
    else:
        query = {"timestamp": {"$regex": date, "$options": "i"}}
        news = search_news(query)
        return [
            (actual_news["title"], actual_news["url"]) for actual_news in news
        ]


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
