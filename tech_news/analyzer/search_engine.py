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
    """Possível buscar uma notícia pela data com sucesso; Ao buscar por uma
    data que não existe, o retorno deve ser uma lista vazia; Ao buscar por uma
    data com formato inválido, deve lançar um erro ValueError com a mensagem
    Data inválida."""

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
    """Possível buscar uma notícia pela fonte com sucesso; Ao buscar por uma
    fonte que não existe, o retorno deve ser uma lista vazia; Possível buscar
    uma notícia tanto pela fonte em maiúsculas como em minúsculas;"""

    myquery = {
        "sources": {"$elemMatch": {"$regex": source, "$options": "i"}}
    }
    search_results = search_news(myquery)

    return [(result["title"], result["url"]) for result in search_results]


# Requisito 9
def search_by_category(category):
    """Possível buscar uma notícia pela categoria com sucesso; Ao buscar por
    uma categoria que não existe, o retorno deve ser uma lista vazia; Possível
    buscar uma notícia tanto pela categoria em maiúsculas como em
    minúsculas;"""

    myquery = {
        "categories": {"$elemMatch": {"$regex": category, "$options": "i"}}
    }
    search_results = search_news(myquery)

    return [(result["title"], result["url"]) for result in search_results]
