import re
from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    title_rpx = re.compile(f".*{title}.*", re.IGNORECASE)
    search = search_news({"title": title_rpx})
    news = []
    for result in search:
        url_text = (result["title"], result["url"])
        news.append(url_text)
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
