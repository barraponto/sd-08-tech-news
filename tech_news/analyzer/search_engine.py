from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    """Seu código deve vir aqui"""

    # https://www.w3schools.com/python/python_mongodb_query.asp
    myquery = {"title": {"$regex": title, "$options": 'i'}}

    search_results = search_news(myquery)
    return [(result["title"], result["url"]) for result in search_results]


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
