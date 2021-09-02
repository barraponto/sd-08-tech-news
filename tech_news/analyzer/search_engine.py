from datetime import datetime
from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    # source: https://docs.mongodb.com/manual/reference/operator/query/regex/
    mongo_query = {"title": {"$regex": title, "$options": "i"}}
    news = search_news(mongo_query)
    tuple_news = [
        (actual_news["title"], actual_news["url"]) for actual_news in news
    ]
    return tuple_news


def is_a_valid_data(date):
    try:
        datetime.strptime(date, "%Y-%m-%d")
        return True
    except ValueError:
        return False


# Requisito 7
def search_by_date(date):
    if is_a_valid_data(date) is False:
        raise ValueError("Data inválida")
    else:
        mongo_query = {"timestamp": {"$regex": date, "$options": "i"}}
        news = search_news(mongo_query)
        tuple_news = [
            (actual_news["title"], actual_news["url"]) for actual_news in news
        ]
        return tuple_news


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
