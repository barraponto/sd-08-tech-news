from tech_news.database import search_news
from datetime import datetime

# Requisito 6


def search_by_title(title):
    news = []
    get_news_title = search_news(
        {"title": {"$regex": title, "$options": "i"}})
    for news_info in get_news_title:
        news.append(tuple([news_info["title"], news_info["url"]]))
    return news


# Requisito 7
def search_by_date(date):
    format_date = "%Y-%m-%d"

    try:
        datetime.strptime(date, format_date)
        news = []
        get_news_by_date = search_news(
            {"timestamp": {"$regex": date}}
        )
        for news_info in get_news_by_date:
            news.append(tuple([news_info["title"], news_info["url"]]))
        return news
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_source(source):
    news = []
    get_news_by_source = search_news(
        {"sources": {"$regex": source, "$options": "i"}}
    )
    for news_info in get_news_by_source:
        news.append(tuple([news_info["title"], news_info["url"]]))
    return news


# Requisito 9
def search_by_category(category):
    news = []
    get_news_by_category = search_news(
        {"categories": {"$regex": category, "$options": "i"}}
    )
    for news_info in get_news_by_category:
        news.append(tuple([news_info["title"], news_info["url"]]))
    return news
