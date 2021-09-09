from tech_news.database import db


# Requisito 6
def search_by_title(title):
    """Seu código deve vir aqui"""
    search_title = list(
        db.news.find(
            {"title": {"$regex": title, "$options": "i"}},
            {"_id": 0, "title": 1, "url": 1},
        )
    )

    if len(search_title) == 0:
        return search_title

    return [(search_title[0]["title"], search_title[0]["url"])]


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
