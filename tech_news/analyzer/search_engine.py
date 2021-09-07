import tech_news.database as db
from datetime import datetime

# Referências:
# https://stackoverflow.com/questions/18039680/django-get-only-date-from-datetime-strptime


# Requisito 6
def search_by_title(title):
    """Seu código deve vir aqui"""
    news = db.find_news()
    result = []

    for info in news:
        if info["title"].lower() == title.lower():
            result.append(
                (info["title"], info["url"])
            )
    return result


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""
    news = db.find_news()
    result = []

    try:
        for info in news:
            if datetime.strptime(
                info['timestamp'], "%Y-%m-%dT%H:%M:%S"
            ).date() == datetime.strptime(
                date, "%Y-%m-%d"
            ).date():
                result.append(
                    (info["title"], info["url"])
                )
            return result
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
