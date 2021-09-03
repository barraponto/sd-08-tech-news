from tech_news.database import find_news
import re
import datetime


# Requisito 6
def search_by_title(title):
    news_list = find_news()
    LIST = []
    for item in news_list:
        if re.search(title, item["title"], re.IGNORECASE):
            result = (item["title"], item["url"])
            LIST.append(result)
    return LIST


# Requisito 7
def search_by_date(date):
    news_list = find_news()
    LIST = []
    try:
        datetime.datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        raise ValueError("Data inválida")
    for item in news_list:
        if re.search(date, item["timestamp"], re.IGNORECASE):
            result = (item["title"], item["url"])
            LIST.append(result)
    return LIST


# Requisito 8
def search_by_source(source):
    news_list = find_news()
    LIST = []
    for item in news_list:
        for value in item["sources"]:
            if re.search(source, value, re.IGNORECASE):
                result = (item["title"], item["url"])
                LIST.append(result)
            else:
                LIST = []
    return LIST


# Requisito 9
def search_by_category(category):
    news_list = find_news()
    LIST = []
    for item in news_list:
        for values in item["categories"]:
            if re.search(category, values, re.IGNORECASE):
                result = (item["title"], item["url"])
                LIST.append(result)
            else:
                LIST = []
    return LIST
