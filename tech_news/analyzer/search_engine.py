# Requisito 6
import tech_news.database as db


def search_by_title(title):
    news = db.find_news()
    list = []
    for x in news:
        if x["title"].lower() == title.lower():
            content = (x["title"], x["url"])
            list.append(content)
    return list


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
