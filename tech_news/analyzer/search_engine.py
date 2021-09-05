from tech_news.database import search_news
from datetime import datetime
import re


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
    source_query = re.compile(f"{source}", re.IGNORECASE)
    news_by_source = search_news({"sources": source_query})
    return [(new["title"], new["url"]) for new in news_by_source]


# Requisito 9
def search_by_category(category):
    category_query = re.compile(f"{category}", re.IGNORECASE)
    news_by_category = search_news({"categories": category_query})
    return [(new["title"], new["url"]) for new in news_by_category]
