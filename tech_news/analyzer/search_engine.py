from tech_news.database import db


# Requisito 6
def search_by_title(title):
    result = list(
        db.news.find(
            {"title": {"$regex": title, "$options": "i"}},
            {"_id": 0, "title": 1, "url": 1},
        )
    )
    if len(result) == 0:
        return result
    else:
        tuplas = result[0] if result is not None else []
        lista = list(tuple(tuplas.values()))
        return [(lista[1], lista[0])]


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
