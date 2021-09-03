import re
import datetime
from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    # https://docs.python.org/pt-br/3/library/re.html
    # Regular expression correspondente ao regex
    rgx = re.compile(f".*{title}.*", re.IGNORECASE)

    search = search_news({"title": rgx})
    news = []
    for result in search:
        title_url = (result["title"], result["url"])
        news.append(title_url)
    return news


# Requisito 7
def search_by_date(date):
    try:
        # https://docs.python.org/pt-br/3/library/datetime.html#strftime-strptime-behavior
        datetime.datetime.strptime(date, "%Y-%m-%d")
        rgx = re.compile(f".*{date}*.")
    except ValueError:
        raise ValueError("Data inválida")
    news = []
    search = search_news({"timestamp": rgx})
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
        rgx = re.compile(f".*{unity_source}.*", re.IGNORECASE)
        search = search_news({"sources": rgx})
        for result in search:
            title_url = (result["title"], result["url"])
            news.append(title_url)
        return news


# Requisito 9
def search_by_category(category):
    news = []
    rgx = re.compile(category, re.IGNORECASE)
    search = search_news({"categories": rgx})
    for result in search:
        title_url = (result["title"], result["url"])
        news.append(title_url)
    return news
    