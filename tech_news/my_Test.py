# from tech_news.database import create_news
# from scraper import (
#     fetch,
#     scrape_noticia,
#     scrape_novidades,
#     scrape_next_page_link,
# )
# import json
# from parsel import Selector
import re


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

# get_tech_news(6)

author = "Kris Gaiato (via nexperts)"
author = re.sub(r"[^\w\s\w][\s\S\w]*", "", author)
author = author.split(" ")
author = (" ").join(author[:-1]) if author[-1] == "" else author
print(author)
