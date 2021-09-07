import requests
import time
from parsel import Selector


def fetch(url):
    try:
        time.sleep(1)
        response = requests.get(url, timeout=3)
        if response.status_code == 200:
            return response.text

        return None
    except requests.exceptions.ReadTimeout:
        return None


resposne = fetch("https://www.tecmundo.com.br/mobilidade-u")


def scrape_noticia(html_content):
    selector = Selector(text=html_content)

    categories = []
    sources = []
    for categorie in selector.css("div#js-categories a::text").getall():
        categories.append(categorie.strip())

    for source in selector.css("div.z--mb-16 div a::text").getall():
        sources.append(source.strip())

    dicionario = {
      "url": selector.css("head link[rel=canonical]::attr(href)").get(),
      "title": selector.css("h1.tec--article__header__title::text").get(),
      "timestamp": selector
      .css("div.tec--timestamp__item time::attr(datetime)").get(),
      "writer": selector.css("a.tec--author__info__link::text").get().strip(),
      "shares_count": int(
        selector.css("div.tec--toolbar__item::text").get().split().pop(0)),
      "comments_count": int(
        selector.css("div.tec--toolbar__item button::attr(data-count)").get()),
      "summary": ''.join(
        selector.css("div.tec--article__body p:nth-child(1) *::text").extract()
      ),
      "sources": sources,
      "categories": categories,
    }

    return dicionario


print(scrape_noticia(resposne))
