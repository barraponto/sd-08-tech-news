from tech_news.database import search_news


# Requisito 6
def search_by_title(titulo):
    db = search_news({"title": titulo.lower().capitalize()})
    lista = []
    for item in db:
        lista = [(item["title"], item["url"])]
    return lista


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
