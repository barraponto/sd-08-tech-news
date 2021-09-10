import tech_news.database as db
from datetime import datetime


# Requisito 6
def search_by_title(title):
    """Seu código deve vir aqui"""
    news = db.find_news()
    return [
        (new["title"], new["url"])

        for new in news
        if new["title"].lower() == title.lower()
    ]


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""
    news = db.find_news()
    try:
        datetime.strptime(date, "%Y-%m-%d").date()
        news_list = []
        for new in news:
            if datetime.strptime(date, "%Y-%m-%d").date() == datetime.strptime(
                new['timestamp'], "%Y-%m-%dT%H:%M:%S"
            ).date():
                # result = (new["title"], new["url"])
                news_list.append((new["title"], new["url"]))
            return news_list
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""
    news = db.find_news()
    source_list = []
    for new in news:
        for source in new["sources"]:
            if source.lower() == source.lower():
                source_list.append((new["title"], new["url"]))
    return source_list


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
    news = db.find_news()
    categories_list = []
    for new in news:
        for category in new["categories"]:
            if category.lower() == category.lower():
                categories_list.append((new["title"], new["url"]))
    return categories_list
