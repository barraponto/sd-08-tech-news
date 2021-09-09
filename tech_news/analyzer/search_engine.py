import tech_news.database as db
from datetime import datetime


# Requisito 6
def search_by_title(title):
    news = db.find_news()
    list = []
    for item in news:
        if item["title"].lower() == title.lower():
            content = (item["title"], item["url"])
            list.append(content)
    return list


# Requisito 7
def search_by_date(date):
    news = db.find_news()
    try:
        datetime.strptime(date, "%Y-%m-%d").date()
        list = []
        for item in news:
            if datetime.strptime(date, "%Y-%m-%d").date() == datetime.strptime(
                item['timestamp'], "%Y-%m-%dT%H:%M:%S"
            ).date():
                result = (item["title"], item["url"])
                list.append(result)
            return list
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_source(source):
    news = db.find_news()
    source_list = []
    for item in news:
        for y in item["sources"]:
            if y.lower() == source.lower():
                result = (item["title"], item["url"])
                source_list.append(result)
    return source_list


# Requisito 9
def search_by_category(category):
    news = db.find_news()
    news_list = []
    for item in news:
        for cat in item["categories"]:
            if cat.lower() == category.lower():
                result = (item["title"], item["url"])
                news_list.append(result)
    return news_list
