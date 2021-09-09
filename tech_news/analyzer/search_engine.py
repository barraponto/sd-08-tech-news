import re
from tech_news.database import find_news


# Requisito 6
def search_by_title(title):
    news = find_news()
    return [
        (single_news["title"], single_news["url"])
        for single_news in news
        if re.match(title, single_news["title"], re.IGNORECASE) is not None
    ]


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
