from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    if title.isupper():
        title = title.capitalize()

    result = search_news({"title": {"$regex": title}})
    array = []

    for noticia in result:
        array.append((noticia["title"], noticia["url"]))

    print(array)

    return array


# Requisito 7
def search_by_date(date):
    


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
