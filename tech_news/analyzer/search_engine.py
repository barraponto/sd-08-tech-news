import tech_news.database as db
from datetime import datetime


# Requisito 6
def search_by_title(title):
    news = db.find_news()
    list = []
    for x in news:
        if x["title"].lower() == title.lower():
            content = (x["title"], x["url"])
            list.append(content)
    return list


# Requisito 7
def search_by_date(date):
    news = db.find_news()
    try:
        datetime.strptime(date, "%Y-%m-%d").date()
        list = []
        for x in news:
            if datetime.strptime(date, "%Y-%m-%d").date() == datetime.strptime(
                x['timestamp'], "%Y-%m-%dT%H:%M:%S"
            ).date():
                result = (x["title"], x["url"])
                list.append(result)
            return list
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_source(source):
    news = db.find_news()
    source_list = []
    for x in news:
        for y in x["sources"]:
            if y.lower() == source.lower():
                result = (x["title"], x["url"])
                source_list.append(result)
    return source_list


# Requisito 9
def search_by_category(category):
    news = db.find_news()
    cat_list = []
    for x in news:
        for y in x["categories"]:
            if y.lower() == category.lower():
                result = (x["title"], x["url"])
                cat_list.append(result)
    return cat_list
