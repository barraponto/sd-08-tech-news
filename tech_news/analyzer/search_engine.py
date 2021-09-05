from tech_news.database import search_news
import datetime


# Requisito 6
def search_by_title(title):
    data = search_news({"title": {"$regex": f"^(?i){title}"}})
    if not data or len(data) == 0:
        return []
    lista_result = []
    for x in data:
        result = (x["title"], x["url"])
        lista_result.append(result)
    return lista_result


# Requisito 7
def search_by_date(date):
    try:
        datetime.datetime.fromisoformat(date).timestamp()

        data = search_news({"timestamp": {"$regex": date}})
        if not data or len(data) == 0:
            print("VAZIO ", data)
            return []
        lista_result = []
        for x in data:
            result = (x["title"], x["url"])
            lista_result.append(result)
        return lista_result
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
