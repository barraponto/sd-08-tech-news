from tech_news.database import search_news
import datetime


# Requisito 6
def search_by_title(title):
    result = search_news({"title": {"$regex": title, "$options": "i"}})
    noticias = []

    for noticia in result:
        noticias.append((noticia["title"], noticia["url"]))

    return noticias


# Requisito 7
def search_by_date(date):
    try:
        datetime.datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        raise ValueError("Data inválida")

    result = search_news({"timestamp": {"$regex": date}})
    noticias = []

    for noticia in result:
        noticias.append((noticia["title"], noticia["url"]))

    return noticias


# Requisito 8
def search_by_source(source):
    result = search_news({"sources": {"$regex": source, "$options": "i"}})
    noticias = []

    for noticia in result:
        noticias.append((noticia["title"], noticia["url"]))

    return noticias


# Requisito 9
def search_by_category(category):
    result = search_news({"categories": {"$regex": category, "$options": "i"}})
    noticias = []

    for noticia in result:
        noticias.append((noticia["title"], noticia["url"]))

    return noticias
