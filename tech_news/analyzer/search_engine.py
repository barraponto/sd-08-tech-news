import tech_news.database as db
from datetime import datetime


# Requisito 6
def search_by_title(title):
    news = db.find_news()
    list = []
    for new in news:
        if new["title"].lower() == title.lower():
            content = (new["title"], new["url"])
            list.append(content)
    return list


# Requisito 7
def search_by_date(date):
    news = db.find_news()
    try:
        datetime.strptime(date, "%Y-%m-%d").date()
        list = []
        for new in news:
            if datetime.strptime(date, "%Y-%m-%d").date() == datetime.strptime(
                new['timestamp'], "%Y-%m-%dT%H:%M:%S"
            ).date():
                result = (new["title"], new["url"])
                list.append(result)
            return list
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_source(source):
    news = db.find_news()
    source_list = []
    for new in news:
        for y in new["sources"]:
            if y.lower() == source.lower():
                result = (new["title"], new["url"])
                source_list.append(result)
    return source_list


# Requisito 9
def search_by_category(category):
    news = db.find_news()
    cat_list = []
    for new in news:
        for y in new["categories"]:
            if y.lower() == category.lower():
                result = (new["title"], new["url"])
                cat_list.append(result)
    return cat_list
    