import re
from datetime import datetime
from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    """Seu código deve vir aqui"""
    results = search_news({"title": re.compile(title, re.IGNORECASE)})
    return [(news["title"], news["url"]) for news in results]


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""
    try:
        datetime.fromisoformat(date).timestamp()
    except ValueError:
        raise ValueError("Data inválida")

    results = search_news({"timestamp": re.compile(date)})
    return [(news["title"], news["url"]) for news in results]


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""
    results = search_news({"sources": re.compile(source, re.IGNORECASE)})
    return [(news["title"], news["url"]) for news in results]


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
    results = search_news({"categories": re.compile(category, re.IGNORECASE)})
    return [(news["title"], news["url"]) for news in results]
