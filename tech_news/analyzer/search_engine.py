from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    request_news = search_news({"title": {"$regex": title, "$options": "i"}})
    if len(request_news) > 0:
        return [(request_news[0]["title"], request_news[0]["url"])]
    else:
        return []


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
