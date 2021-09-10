from tech_news.database import search_news, aggregate
from datetime import datetime


# Requisito 6
def search_by_title(titulo):
    db = search_news({"title": titulo.lower().capitalize()})
    lista = []
    for item in db:
        lista = [(item["title"], item["url"])]
    return lista


# Requisito 7
def search_by_date(date):
    format = "%Y-%m-%d"
    try:
        datetime.strptime(date, format)
    except ValueError:
        raise ValueError("Data inválida")

    db = aggregate(date)
    lista = []
    for item in db:
        lista = [(item["title"], item["url"])]
    print('lista')
    print(lista)
    return lista


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
