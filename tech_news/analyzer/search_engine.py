from tech_news.database import search_news


def format_news(new):
    return (new['title'], new['url'])


# Requisito 6
def search_by_title(title):
    query = {'title': {'$regex': f'.*{title}.*', '$options': "i"}}
    news = search_news(query)

    return [format_news(new) for new in news]


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
