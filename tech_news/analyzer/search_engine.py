import re
from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    """Seu código deve vir aqui"""
    query = re.compile(f"{title}", re.IGNORECASE)
    news_by_title = search_news({"title": query})
    news_tuple_list = []
    for news in news_by_title:
        title_url_tuple = (news["title"], news["url"])
        news_tuple_list.append(title_url_tuple)
    return news_tuple_list


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
