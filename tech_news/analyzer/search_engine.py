from tech_news.database import search_news
import re


# Requisito 6
def search_by_title(title):
    """https://
    www.geeksforgeeks.org/name-validation-using-ignorecase-in-python-regex/"""
    find_title = {"title": re.compile(title, re.IGNORECASE)}
    get_news_by_title = search_news(find_title)
    news_list = []
    for news in get_news_by_title:
        news_list.append((news["title"], news["url"]))
    return news_list


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
