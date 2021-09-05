from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    news = search_news({"title": {"$regex": title, "$options": "si"}})
    searchResults = list()

    for item in news:
        searchResults.append((item["title"], item["url"]))

    return searchResults


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
