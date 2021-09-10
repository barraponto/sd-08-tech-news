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
def date_validation(date):
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        return ValueError("Data inválida")


def search_by_date(date):
    """Seu código deve vir aqui"""
    news = db.find_news()
    date_validation(date)
    return [
      (new["title"], new["url"])

      for new in news
      if datetime.strptime(date, "%Y-%m-%d").date()
      == datetime.strptime(new["timestamp"], "%Y-%m-%dT%H:%M:%S").date()
    ]


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
