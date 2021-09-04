from scraper import fetch, scrape_noticia
import json
from parsel import Selector

expexted = ""
with open("tests/assets/cached_news.json") as arquivo:
    all_news = json.load(arquivo)
    expexted = all_news[15]

htmls2 = fetch(
    str(
        "https://www.tecmundo.com.br/"
        "dispositivos-moveis/215327-pixel-5a-tera-lancamento"
        "-limitado-devido-escassez-chips.htm"
    )
)

result1 = scrape_noticia(htmls2)

for k in expexted:
    print(k, " -- ", expexted[k])
    print(k, " -- ", result1[k], end="\n\n")

print(end="\n\n")
selector1 = Selector(text=htmls2)

summary = (
    selector1.xpath("//div[contains(@class, 'tec--article__body')][1]/p[1]")
    .css("*::text")
    .getall()
)

print(summary)
