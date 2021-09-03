import sys
from tech_news.analyzer.ratings import top_5_categories, top_5_news
from tech_news.scraper import get_tech_news
from tech_news.analyzer.search_engine import (
    search_by_category,
    search_by_date,
    search_by_source,
    search_by_title,
)


# Requisito 12
def _input_option(number):
    entrer = ""
    if number == 0:
        entrer = input("Digite quantas notícias serão buscadas:")
        num = _is_number(entrer)
        print(num)
        get_tech_news(num)
    elif number == 1:
        entrer = input("Digite o título:")
        search_by_title(entrer)
    elif number == 2:
        entrer = input("Digite a data no formato aaaa-mm-dd:")
        search_by_date(entrer)
    elif number == 3:
        entrer = input("Digite a fonte:")
        search_by_source(entrer)
    else:
        entrer = input("Digite a categoria:")
        search_by_category(entrer)
    # elif number == 5:
    #     entre = input("Digite quantas notícias serão buscadas:")
    # elif number == 6:
    #     entre = input("Digite quantas notícias serão buscadas:")
    # elif number == 7:
    #     entre = input("Digite quantas notícias serão buscadas:")
    return entrer


def _is_number(entrer):
    number = None
    try:
        number = int(entrer)
    except TypeError:
        _error_mensage()
        return None
    except ValueError:
        _error_mensage()
        return None
    return number


def _error_mensage():
    print("Opção inválida", file=sys.stderr)


def analyzer_menu():
    entrer = input(
        """Selecione uma das opções a seguir:
 0 - Popular o banco com notícias;
 1 - Buscar notícias por título;
 2 - Buscar notícias por data;
 3 - Buscar notícias por fonte;
 4 - Buscar notícias por categoria;
 5 - Listar top 5 notícias;
 6 - Listar top 5 categorias;
 7 - Sair."""
    )
    number = _is_number(entrer)
    if number is None:
        return None
    if 0 <= number and number <= 4:
        entrer = _input_option(number)
    if number == 5:
        top_5_news()
    if number == 6:
        top_5_categories()
    elif number > 7:
        _error_mensage()
    else:
        print("Encerrando script")
        pass
