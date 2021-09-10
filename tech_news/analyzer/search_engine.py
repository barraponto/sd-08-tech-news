from tech_news.database import search_news
import re


# Requisito 6
def search_by_title(title):
    found_news = search_news(
        {"title": re.compile("^" + title + "$", re.IGNORECASE)}
    )
    news_data = []

    for news in found_news:
        news_data.append((news["title"], news["url"]))

    return news_data


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
