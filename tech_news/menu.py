import sys
from tech_news.analyzer.ratings import top_5_categories, top_5_news
from tech_news.scraper import get_tech_news
from tech_news.analyzer.search_engine import (
    search_by_category,
    search_by_date,
    search_by_source,
    search_by_title,
)


def _input_option(self, number):
    text = {
        0: "Digite quantas notícias serão buscadas:",
        1: "Digite o título:",
        2: "Digite a data no formato aaaa-mm-dd:",
        3: "Digite a fonte:",
        4: "Digite a categoria:",
    }
    load = input(text[self.type])
    if number == 1:
        response = _is_number(load)
        if response is None:
            return None
    else:
        response = load
    _fist_case(number, response)
    return None


def _fist_case(number, load):
    case = {
        0: get_tech_news(load),
        1: search_by_title(load),
        2: search_by_date(load),
        3: search_by_source(load),
        4: search_by_category(load)
    }
    return case[number]


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
    entre_number = {
        5: top_5_news(),
        6: top_5_categories(),
        7: print("Encerrando script")
    }
    number = _is_number(entrer)
    if number is None:
        return None
    if 0 <= number and number <= 4:
        entrer = _input_option(number)
    elif number <= 7:
        return entre_number[number]
    elif number > 7:
        _error_mensage()
        return None
    else:
        print("Encerrando script")
        pass
