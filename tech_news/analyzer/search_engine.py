from tech_news.database import search_news

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
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
