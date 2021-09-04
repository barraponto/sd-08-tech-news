from scraper import fetch
from parsel import Selector

# expexted = ""
# with open("tests/assets/cached_news.json") as arquivo:
#     all_news = json.load(arquivo)
#     expexted = all_news[15]
url = "https://www.tecmundo.com.br/novidades"

while True:
    htmls1 = fetch(url)

    selector1 = Selector(text=htmls1)

    url = selector1.xpath(
        str(
            "//a[@class='tec--btn tec--btn--lg "
            "tec--btn--primary z--mx-auto z--mt-48']/@href"
        )
    ).get()

    print(url)
    if not url:
        print("FIM")
        break
# [print(x, end="\n\n") for x in list_links_noticias]
