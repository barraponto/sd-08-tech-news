import tech_news.database as db


# Requisito 6
def search_by_title(title):
    """Seu código deve vir aqui"""
    news = db.find_news()
    result = []

    for info in news:
        if info["title"].lower() == title.lower():
            result.append(
                (info["title"], info["url"])
            )
    return result


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
