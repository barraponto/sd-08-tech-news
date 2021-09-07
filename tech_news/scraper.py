import requests
from parsel import Selector
import time
from requests.exceptions import HTTPError


# Requisito 1
def fetch(url):
    try:
        time.sleep(1)
        site = requests.get(url, timeout=3)
    except requests.Timeout:
        return None
    try:
        site.raise_for_status()
    except HTTPError:
        return None
    return site.text


def scrape_noticia(html_content):
    """Canonical tag é uma marcação inserida no código de páginas da web
    para definir que elas são um conteúdo original. Essa tag serve
    diretamente para a leitura dos algoritmos de motores de busca, como
    o Google e o Yahoo e funciona como um alerta de que aquela é a página
    à qual os usuários devem ser redirecionados ao realizarem uma pesquisa
    nesses sites. É comum encontrar páginas iguais, mas com URLs diferentes,
    isso dentro de um mesmo site. Essas variações de endereço acontecem,
    muitas vezes, de forma natural na construção do site, mas podem ser
    prejudiciais na hora de rankear a página.
    A canonical tag mostra ao algoritmo qual é prioritária, ou seja, a
    página original que será mostrada em resultados de pesquisas.
    fonte: https://rockcontent.com/br/blog/canonical-tag/"""
    selector = Selector(text=html_content)
    url = selector.css("link[rel=canonical]::attr(href)").get()

    # extrai o texto do h1 da classe que está selecionada
    title = selector.css("h1.tec--article__header__title::text").get()

    # extrai da tag time o datetime. A data já está formatada no site
    timestamp = selector.css("time::attr(datetime)").get()

    # Extrai o nome do autor. Apenas a classe após o href é suficiente
    # É necessário usar o strip() pois ao final do nome um espaço é retornado
    writer = selector.css(".tec--author__info__link::text").get().strip()

    # Extrai a quantidade de comentários usando a classe tec--toolbar__item,
    # o id js-comments-btn e o atributo 'data-count'
    comments_count = int(
        selector.css(
            "div.tec--toolbar__item #js-comments-btn ::attr(data-count)"
        ).get()
    )

    # Tive dificuldade para entender onde achar...
    # Deve extrair o número de compartilhamento da notícia.
    # A pseudo-classe CSS :nth-child() seleciona elementos
    #  com base em suas posições em um grupo de
    # elementos irmãos.
    # fonte (https://developer.mozilla.org/pt-BR/docs/Web/CSS/:nth-child)
    shares_count = int(
        selector.css(".tec--toolbar__item::text").get().strip().split()[0]
    )

    # extrai o texto da tag p e pseudo-classe nth-child(1)
    # Dúvida: PQ com o uso do >
    # fonte: (https://stackoverflow.com/questions/38182972/
    # python-scrapy-cant-get-pseudo-class-not)
    summary = "".join(
        selector.css(
            "div.tec--article__body p:nth-child(1) ::text"
        ).getall()
    )

    # cria uma lista com as fontes da notícia
    # dúvida: Porque se eu adicionar div à classe tec--badge
    # ex: "div.z--mb-16 div.tec--badge::text" não funciona?
    sources = []
    source_list = selector.css("div.z--mb-16 .tec--badge::text").getall()
    for source in source_list:
        sources.append(source.strip())

    # cria a lista de categorias através do id js-categories e
    # acessando o texto da tag a
    categories = []
    categories_list = selector.css("#js-categories a *::text").getall()
    for category in categories_list:
        categories.append(category.strip())

    result = {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "shares_count": shares_count,
        "comments_count": comments_count,
        "summary": summary,
        "sources": sources,
        "categories": categories,
    }
    return result


# Requisito 3
# Pega a classe "tec--list__item" da div
# segue passando pela tag h3 até o a href...
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    return selector.css(
            "div.tec--list__item h3 a::attr(href)"
    ).getall()


# Requisito 4
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    try:
        # Pegar o href do botão que tem a classe .tec--btn
        return selector.css(".tec--btn::attr(href)").get()
    except Exception:
        return None


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
