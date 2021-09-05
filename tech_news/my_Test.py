from tech_news.database import search_news

# import time
import datetime

# import json
# from parsel import Selector
# import re


# def get_tech_news(amount):
#     url = "https://www.tecmundo.com.br/novidades"
#     lista_info_noticias = []
#     print("URL ATUAL -->", url)
#     while True:
#         str_html_novidades = fetch(url)

#         links_noticias_fetch = scrape_novidades(str_html_novidades)
#         print("\n\n", links_noticias_fetch, end="\n\n")
#         print("\n\n", end="\n\n")
#         for link in links_noticias_fetch:
#             if len(lista_info_noticias) < amount:
#                 print("URL ----- AGORA -->  ", link)
#                 html_noticia = fetch(link)
#                 info_noticia = scrape_noticia(html_noticia)
#                 print(info_noticia, end="\n\n")
#                 lista_info_noticias.append(info_noticia)
#             else:
#                 break

#         print("---------------------------------")
#         url = scrape_next_page_link(str_html_novidades)
#         print("NEXT URL -->  ", url)
#         if len(lista_info_noticias) == amount:
#             break

#     create_news(lista_info_noticias)


# url = str(
#     "https://www.tecmundo.com.br/produto/224410-qualcomm-snapdragon"
#     "-898-processador-tem-novos-detalhes-descobertos.htm"
# )

# html_str = fetch(url)

# selector = Selector(text=html_str)

# data = json.loads(
#     selector.xpath(str("//script[contains(@type, 'application/ld+json')]"))
#     .css("::text")
#     .getall()[1]
# )

# if data.get("author"):
#     data = data["author"]["name"]
# else:
#     data = data.get("name")

# print(data)

# get_tech_news(30)

# find_news, search_news, get_collection
# def insert_or_update(notice):
#     return (
#         db.news.update_one(
#             {"url": notice["url"]}, {"$set": notice}, upsert=True
#         ).upserted_id
#         is not None
#     )


# def find_news():
#     return list(db.news.find({}, {"_id": False}))


# data = search_news({"title": {"$regex": "tem"}})
# print(data)
# lista_result = []
# for x in data:
#     result = (x["title"], x["url"])
#     lista_result.append(result)
# [print(x, end="\n\n") for x in data]

# [print(x, end="\n\n") for x in lista_result]


def search_by_title(date):
    try:
        y, m, d = date.split("-")
        print(y, m, d)
        datetime.date(int(y), int(m), int(d))

        data = search_news({"timestamp": {"$regex": date}})
        if not data or len(data) == 0:
            print("VAZIO ", data)
            return []
        lista_result = []
        for x in data:
            result = (x["timestamp"], x["url"])
            lista_result.append(result)
        return lista_result
    except ValueError:
        return "Data inválida"


d = search_by_title("21-12-1980")

print(d)
