from tech_news.database import search_news, get_collection, find_news
from tech_news.scraper import get_tech_news

# import time
# import datetime

# import json
# from parsel import Selector
# import re

# get_tech_news(100)
# lista = [
#     {"title": "B1", "total": 6},  # 2
#     {"title": "A1", "total": 3},  # 3
#     {"title": "Z1", "total": 0},  # 2
#     {"title": "H1", "total": 2},  # 4
#     {"title": "F1", "total": 3},  # 5
#     {"title": "E1", "total": 5},  # 5
#     {"title": "T1", "total": 0},  # 2
#     {"title": "I1", "total": 2},  # 3
#     {"title": "M1", "total": 1},  # 5
#     {"title": "S1", "total": 7},  # 5
#     {"title": "G1", "total": 5},  # 5
#     {"title": "B1", "total": 10},  # 2
#     {"title": "H1", "total": 4},  # 5
#     {"title": "A1", "total": 1},  # 5
#     {"title": "B1", "total": 1},  # 2
# ]


# def shellSort():
#     h = 1
#     n = len(lista)

#     while h > 0:
#         for i in range(h, n):
#             c = lista[i]
#             j = i

#             while j >= h and c["total"] > lista[j - h]["total"]:
#                 lista[j] = lista[j - h]
#                 j = j - h
#                 lista[j] = c

#         h = int(h / 2.2)

#     # new_list = sorted(lista[:5], key=lambda x: x["title"])
#     new_list = lista.copy()

#     for x in range(n):
#         for y in range(x, n):
#             n_x = lista[x]["total"]
#             n_y = lista[y]["total"]

#             if x != y and n_x == n_y:

#                 list_sorted = sorted(
#                     [lista[x], lista[y]], key=lambda x: x["title"]
#                 )

#                 lista[x] = list_sorted[0]
#                 lista[y] = list_sorted[1]

#     return new_list


# sortedByName = sorted(employees, key=lambda x: x.name)

# new_list = shellSort()
# [print(x, end="\n\n") for x in lista]
# print("\n\n")
# [print(x, end="\n\n") for x in new_list]


# lista = find_news()


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


def top_5_news():
    lista_news = shellSort()

    # ordenação alfabética em caso de empate
    alphabetical_order(lista_news)
    return lista_news


[print(x, end="\n\n") for x in top_5_news()]
