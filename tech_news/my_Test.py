from scraper import fetch
from parsel import Selector

# expexted = ""
# with open("tests/assets/cached_news.json") as arquivo:
#     all_news = json.load(arquivo)
#     expexted = all_news[15]

htmls1 = fetch(str("https://www.tecmundo.com.br/novidades"))

selector1 = Selector(text=htmls1)

list_links_noticias = selector1.xpath(
    str(
        "//div[@class='tec--list__item']"
        "//figure//a[@class='tec--card__thumb__link']/@href"
    )
).getall()

[print(x, end="\n\n") for x in list_links_noticias]
