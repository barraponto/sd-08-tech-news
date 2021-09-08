from tech_news.database import search_news

# Requisito 6


def search_by_title(title):
    news = []
    get_news_title = search_news(
        {"title": {"$regex": title, "$options": "i"}})
    for news_info in get_news_title:
        news.append(tuple([news_info["title"], news_info["url"]]))
    return news


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
