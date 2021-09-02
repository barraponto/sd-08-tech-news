from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    mongo_query = {"title": {"$regex": title, "$options": "i"}}
    news = search_news(mongo_query)
    tuple_news = [
        (actual_news["title"], actual_news["url"]) for actual_news in news
    ]
    return tuple_news


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
