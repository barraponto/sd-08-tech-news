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
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
