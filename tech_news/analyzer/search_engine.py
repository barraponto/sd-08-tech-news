from tech_news.database import search_news
from datetime import datetime


# Requisito 6
def search_by_title(title):
    """Possível buscar uma notícia pelo título com sucesso; Ao buscar por um
    título que não existe, o retorno é uma lista vazia; Possível buscar uma
    notícia com sucesso, tanto pelo título em maiúsculas como em minúsculas."""

    # https://www.w3schools.com/python/python_mongodb_query.asp
    myquery = {"title": {"$regex": title, "$options": "i"}}

    search_results = search_news(myquery)
    return [(result["title"], result["url"]) for result in search_results]


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""

    # https://qastack.com.br/programming/16870663/how-do-i-validate-a-date-string-format-in-python
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Data inválida")

    # https://www.w3schools.com/python/python_mongodb_query.asp
    myquery = {"timestamp": {"$regex": date}}

    search_results = search_news(myquery)
    return [(result["title"], result["url"]) for result in search_results]


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""

    myquery = {
        "sources": {"$elemMatch": {"$regex": source, "$options": "i"}}
    }
    search_results = search_news(myquery)

    return [(result["title"], result["url"]) for result in search_results]


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
