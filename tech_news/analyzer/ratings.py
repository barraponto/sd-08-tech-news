# Requisito 10
from tech_news.database import find_news
from tech_news.analyzer.search_engine import serealize


def shellSort():
    # fonte do algoritmo de ordenação
    # https://pt.wikipedia.org/wiki/Shell_sort
    lista = find_news()
    h = 1
    n = len(lista)
    if n < 5:
        return lista

    while h > 0:
        for i in range(h, n):
            c = lista[i]
            j = i
            c_total = c["shares_count"] + c["comments_count"]
            j_total = (
                lista[j - h]["shares_count"] + lista[j - h]["comments_count"]
            )
            while j >= h and c_total > j_total:
                lista[j] = lista[j - h]
                j = j - h
                lista[j] = c
                j_total = (
                    lista[j - h]["shares_count"]
                    + lista[j - h]["comments_count"]
                )

        h = int(h / 2.2)
    result_list = lista[:5]
    return result_list


def alphabetical_order(lista_news):
    n = len(lista_news)
    for x in range(n):
        for y in range(x, n):
            n_x = (
                lista_news[x]["shares_count"] + lista_news[x]["comments_count"]
            )
            n_y = (
                lista_news[y]["shares_count"] + lista_news[y]["comments_count"]
            )

            if x != y and n_x == n_y:

                list_sorted = sorted(
                    [lista_news[x], lista_news[y]], key=lambda x: x["title"]
                )

                lista_news[x], lista_news[y] = list_sorted


# Requisito 10
def top_5_news():
    lista_news = shellSort()

    # ordenação alfabética em caso de empate
    alphabetical_order(lista_news)
    return serealize(lista_news)


# Requisito 11
def serialize_categories(top_categories):
    top_categories.sort(key=lambda x: x[0])
    top_categories = [categories[0] for categories in top_categories]
    return top_categories


def sorted_categories(array_news):
    top_categories = dict()
    for new_tec in array_news:
        if not new_tec["categories"] is None and len(new_tec) > 0:
            for categories in new_tec["categories"]:
                if not top_categories.get(categories):
                    top_categories.update({categories: 1})
                else:
                    top_categories[categories] = top_categories[categories] + 1
    top_categories = sorted(
        top_categories.items(), key=lambda x: x[1], reverse=True
    )
    return top_categories


def top_5_categories():
    array_news = find_news()
    length = len(array_news)
    if length == 0:
        return []

    return serialize_categories(sorted_categories(array_news))[:5]
