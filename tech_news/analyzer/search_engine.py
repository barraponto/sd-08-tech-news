from datetime import datetime
import tech_news.database as db


# Requisito 6
def search_by_title(title):
    query = db.search_news({"title": {"$regex": title, "$options": "i"}})
    results = []

    for value in query:
        results.append(((value["title"], value["url"])))

    return results


# Requisito 7
def search_by_date(date):
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Data inválida")

    query = db.search_news({"timestamp": {"$regex": date}})
    results = []

    for value in query:
        results.append((value["title"], value["url"]))

    return results


# Requisito 8
def search_by_source(source):
    query = db.search_news({"sources": {"$regex": source, "$options": "i"}})
    results = []

    for value in query:
        results.append(((value["title"], value["url"])))

    return results


# Requisito 9
def search_by_category(category):
    query = db.search_news(
        {"categories": {"$regex": category, "$options": "i"}}
    )
    results = []

    for value in query:
        results.append(((value["title"], value["url"])))

    return results
