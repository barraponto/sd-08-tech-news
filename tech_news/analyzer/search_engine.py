from tech_news.database import db
from datetime import datetime


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
    try:
        formated_date = datetime.strptime(date, "%Y-%m-%d")
        year = formated_date.strftime("%Y")
        month = formated_date.strftime("%m")
        day = formated_date.strftime("%d")
        datetime(int(year), int(month), int(day))
        search_date = list(
            db.news.find(
                {"timestamp": {"$regex": date}},
                {"_id": 0, "title": 1, "url": 1},
            )
        )
        if len(search_date) == 0:
            return search_date
        return [(search_date[0]["title"], search_date[0]["url"])]
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""
    search_source = list(
        db.news.find(
            {"sources": {"$elemMatch": {"$regex": source, "$options": "i"}}},
            {"_id": 0, "title": 1, "url": 1},
        )
    )
    if len(search_source) == 0:
        return search_source
    return [(search_source[0]["title"], search_source[0]["url"])]


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
