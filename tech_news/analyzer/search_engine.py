from tech_news.database import search_news
from datetime import datetime

# https://kb.objectrocket.com/mongo-db/how-to-query-mongodb-documents-with-regex-in-python-362
# https://docs.python.org/pt-br/3/library/time.html#module-time
# https://www.kite.com/python/answers/how-to-validate-a-date-string-format-in-python
# https://www.programiz.com/python-programming/regex
# https://docs.python.org/pt-br/3/library/re.html?highlight=string%20formatar


# Requisito 6
def search_by_title(title):
    search_result = []
    query = {"title": {"$regex": title, "$options": "i"}}
    results = search_news(query)
    for result in results:
        search_result.append((result["title"], result["url"]))
    return search_result


def isvalid_date(date):
    format = "%Y-%m-%d"
    try:
        datetime.strptime(date, format)
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 7
def search_by_date(date):
    search_result = []
    isvalid_date(date)
    query = {"timestamp":  {"$regex": date}}
    results = search_news(query)
    for result in results:
        search_result.append((result["title"], result["url"]))
    return search_result


# Requisito 8
def search_by_source(source):
    search_result = []
    query = {"sources":  {"$regex": source, "$options": "i"}}
    results = search_news(query)
    for result in results:
        search_result.append((result["title"], result["url"]))
    return search_result


# Requisito 9
def search_by_category(category):
    search_result = []
    query = {"categories":  {"$regex": category, "$options": "i"}}
    results = search_news(query)
    for result in results:
        # print(result)
        search_result.append((result["title"], result["url"]))
    return search_result
