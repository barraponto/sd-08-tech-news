from datetime import datetime
import tech_news.database as db


# Requisito 6
def search_by_title(title):
    query_1 = db.search_news({"title": {"$regex": title, "$options": "i"}})
    results = []

    for value in query_1:
        results.append(((value["title"], value["url"])))

    return results


# Requisito 7
def search_by_date(date):
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Data inválida")

    query_2 = db.search_news({"timestamp": {"$regex": date}})
    results = []

    for value in query_2:
        results.append((value["title"], value["url"]))

    return results


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
