from tech_news.database import search_news
import re
from datetime import datetime


# Requisito 6
def search_by_title(title):
    """usado com base no site https://
    www.geeksforgeeks.org/name-validation-using-ignorecase-in-python-regex/"""
    find_title = {"title": re.compile(title, re.IGNORECASE)}
    get_news_by_title = search_news(find_title)
    news_list = []
    for news in get_news_by_title:
        news_list.append((news["title"], news["url"]))
    return news_list


# Requisito 7
def search_by_date(date):
    """usado com base no site https://python.hotexamples.com/examples/mx/DateTime/
    strptime/python-datetime-strptime-method-examples.html"""
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Data inválida")
    else:
        news = search_news({"timestamp": re.compile(date)})
        results_list = []
        for new in news:
            results_list.append((new["title"], new["url"]))
        return results_list


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
