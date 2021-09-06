import tech_news.database as db


# Requisito 6
def search_by_title(title):
    """Seu código deve vir aqui"""
    news = db.find_news()
    news_list = []
    for item in news:
        if item["title"].lower() == title.lower():
            content = (item["title"], item["url"])
            news_list.append(content)
    return news_list


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
