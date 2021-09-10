import tech_news.database as db
from tech_news.database import search_news
from datetime import datetime
import re


# Requisito 6
def search_by_title(title):
    news = db.find_news()
    news_list = []
    for item in news:
        if item["title"].lower() == title.lower():
            content = (item["title"], item["url"])
            news_list.append(content)
    return news_list


# Requisito 7
def search_by_date(date):
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
    news = db.find_news()
    news_list = []
    for item in news:
        for src in item["sources"]:
            if src.lower() == source.lower():
                content = (item["title"], item["url"])
                news_list.append(content)
    return news_list


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
