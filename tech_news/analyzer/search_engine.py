import re
import datetime
from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    title_rpx = re.compile(f".*{title}.*", re.IGNORECASE)
    search = search_news({"title": title_rpx})
    news = []
    for result in search:
        url_text = (result["title"], result["url"])
        news.append(url_text)
    return news


# Requisito 7
def search_by_date(date):
    try:
        datetime.datetime.strptime(date, "%Y-%m-%d")
        date_rpx = re.compile(f".*{date}*.")
    except ValueError:
        raise ValueError("Data inválida")
    news = []
    search = search_news({"timestamp": date_rpx})
    if search:
        for result in search:
            title_url = (result["title"], result["url"])
            news.append(title_url)
        return news
    else:
        return []


# Requisito 8
def search_by_source(source):
    news = []
    for unity_source in source:
        source_rgx = re.compile(f".*{unity_source}.*", re.IGNORECASE)
        search = search_news({"sources": source_rgx})
        for result in search:
            title_url = (result["title"], result["url"])
            news.append(title_url)
        return news


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
