from tech_news.database import search_news
import datetime

# https://kb.objectrocket.com/mongo-db/how-to-query-mongodb-documents-with-regex-in-python-362


# Requisito 6
def search_by_title(title):
    search_result =[]
    query = {"title": {"$regex": title, "$options": "i"}}
    results = search_news(query)
    for result in results:
        search_result.append((result["title"], result["url"]))
    return search_result


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
