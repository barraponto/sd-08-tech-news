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
    result = find_news()
    all_categories = []
    categories = []

    for categorie in result:
        all_categories = [*all_categories, *categorie["categories"]]

    for categorie in all_categories:
        count = 0
        for categorie2 in all_categories:
            if categorie == categorie2:
                count = count + 1

        categories.append({"categorie": categorie, "count": count})

    categories.sort(key=operator.itemgetter("count", "categorie"))

    top_5 = list(map(return_categorie, categories))
    return top_5[:5]


def return_categorie(categorie):
    return categorie["categorie"]
