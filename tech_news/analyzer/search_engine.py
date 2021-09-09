import re
from datetime import datetime
from tech_news.database import find_news, search_news


# Requisito 6
def search_by_title(title):
    news = find_news()
    return [
        (single_news["title"], single_news["url"])
        for single_news in news
        if re.match(title, single_news["title"], re.IGNORECASE) is not None
    ]


# Requisito 7
def search_by_date(date):
    news = find_news()
    filtered_news = []
    try:
        date_object = datetime.strptime(date, "%Y-%m-%d")
        filtered_news = [
            (single_news["title"], single_news["url"]) for single_news in news
            if date_object.date() == datetime.strptime(
                single_news["timestamp"], "%Y-%m-%dT%H:%M:%S").date()]
    except (AssertionError, ValueError):
        raise ValueError("Data inválida")
    return filtered_news


# Requisito 8
def search_by_source(source):
    filtered_news = search_news({
        "sources": re.compile(source, re.IGNORECASE)})
    return [
        (single_news["title"], single_news["url"])
        for single_news in filtered_news]


# Requisito 9
def search_by_category(category):
    filtered_news = search_news({
        "categories": re.compile(category, re.IGNORECASE)})
    return [
        (single_news["title"], single_news["url"])
        for single_news in filtered_news]
