from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    """Seu código deve vir aqui"""
    query = {"title": {"$regex": f".*{title}*.", "$options": "-i"}}
    news_list = search_news(query)
    tuples_list = [(news["title"], news["url"]) for news in news_list]

    return tuples_list


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""
    year = date.split("-")[0]
    if int(year) < 2000 or len(year) != 4:
        raise ValueError("Data inválida")
    query = {"timestamp": {"$regex": f".*{date}.*"}}
    news_list = search_news(query)
    tuples_list = [(news["title"], news["url"]) for news in news_list]

    return tuples_list


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
