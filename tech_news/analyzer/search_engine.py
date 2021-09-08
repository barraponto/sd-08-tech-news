import re
from tech_news.database import search_news


def format(news_list):
    return [
        (list["title"], list["url"]) for list in news_list
        ]


# Requisito 6
def search_by_title(title):
    """Seu código deve vir aqui"""
    news = search_news({"title": re.compile(title, re.IGNORECASE)})
    return format(news)


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
