from tech_news.database import search_news
import re
from datetime import datetime


# Requisito 6
def search_by_title(title):
    """Seu código deve vir aqui"""
    # consulta na documentacao:
    # https://docs.python.org/pt-br/3.8/howto/regex.html
    title_regex = re.compile(title, re.IGNORECASE)
    query = {"title": title_regex}
    news_by_title = search_news(query)
    return [(news['title'], news['url']) for news in news_by_title]


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""
    try:
        # consulta fonte:
        # https://stackoverflow.com/questions/16870663/how-do-i-validate-a-date-string-format-in-python/16870699
        datetime.strptime(date, "%Y-%m-%d")
        dateRegex = fr'^{date}'
        date_regex = re.compile(dateRegex)
        query = {"timestamp": date_regex}
        news_by_title = search_news(query)
        return [(news['title'], news['url']) for news in news_by_title]
    except (ValueError):
        raise ValueError('Data inválida')


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
