from tech_news.database import find_news
import operator


# Requisito 10
def top_5_news():
    result = find_news()
    noticias = []
    for noticia in result:
        noticia["sum"] = noticia["shares_count"] + noticia["comments_count"]

    result.sort(key=operator.itemgetter("sum"), reverse=True)

    for noticia in result:
        noticias.append((noticia["title"], noticia["url"]))

    return noticias[:5]


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
