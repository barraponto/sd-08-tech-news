from tech_news.database import search_news
import datetime


def serealize(list_noticias):
    return [(x["title"], x["url"]) for x in list_noticias]


# Requisito 6
def search_by_title(title):
    data = search_news({"title": {"$regex": f"^(?i){title}"}})
    if not data or len(data) == 0:
        return []
    return serealize(data)


# Requisito 7
def search_by_date(date):
    try:
        datetime.datetime.fromisoformat(date).timestamp()

        data = search_news({"timestamp": {"$regex": date}})
        if not data or len(data) == 0:
            return []
        return serealize(data)
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_source(source):
    try:
        data = search_news({"sources": {"$regex": f"^(?i){source}"}})
        if not data or len(data) == 0:
            return []
        return serealize(data)
    except Exception:
        return []


# Requisito 9
def search_by_category(category):
    try:
        data = search_news({"categories": {"$regex": f"^(?i){category}"}})
        if not data or len(data) == 0:
            return []
        return serealize(data)
    except Exception:
        return []
