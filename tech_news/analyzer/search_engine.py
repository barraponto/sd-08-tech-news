from tech_news.database import search_news
from datetime import datetime

# Requisito 6
def search_by_title(title):
    news = search_news({"title": {"$regex": title, "$options": "i"} })
    return [(news["title"], news["url"]) for news in news ]


# Requisito 7
def search_by_date(date):
    try:
        datetime.fromisoformat(date)
    except ValueError:
        raise ValueError("Data inválida")
    news = search_news({"timestamp": {"$regex": date, "$options": "i"} })
    return [(news["title"], news["url"]) for news in news ]


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
