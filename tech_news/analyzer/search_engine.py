from tech_news.database import search_news
import re
import datetime


def extract_values(all_news):
    news_data = []

    for news in all_news:
        news_data.append((news["title"], news["url"]))

    return news_data


# Requisito 6
def search_by_title(title):
    found_news = search_news(
        {"title": re.compile("^" + title + "$", re.IGNORECASE)}
    )

    return extract_values(found_news)


# Requisito 7
def search_by_date(date):
    try:
        datetime.datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Data inválida")

    found_news = search_news(
        {"timestamp": re.compile("^" + date, re.IGNORECASE)}
    )

    return extract_values(found_news)


# Requisito 8
def search_by_source(source):
    source_regex = re.compile("^" + source + "$", re.IGNORECASE)
    found_news = search_news({"sources": source_regex})

    return extract_values(found_news)


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
