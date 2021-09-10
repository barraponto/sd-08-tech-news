import sys
from tech_news.scraper import get_tech_news
from tech_news.analyzer.search_engine import (
    search_by_title,
    search_by_date,
    search_by_source,
    search_by_category,
)
from tech_news.analyzer.ratings import top_5_news, top_5_categories


# Requisito 12
def analyzer_menu():
    """Seu código deve vir aqui"""

    menu = """
Selecione uma das opções a seguir:
 0 - Popular o banco com notícias;
 1 - Buscar notícias por título;
 2 - Buscar notícias por data;
 3 - Buscar notícias por fonte;
 4 - Buscar notícias por categoria;
 5 - Listar top 5 notícias;
 6 - Listar top 5 categorias;
 7 - Sair.
    """

    menu_instruction = {
        "0": (
            "Digite quantas notícias serão buscadas:",
            lambda amount: get_tech_news(int(amount))),
        "1": (
            "Digite o título:",
            lambda title: search_by_title(title)),
        "2": (
            "Digite a data no formato aaaa-mm-dd:",
            lambda date: search_by_date(date)),
        "3": (
            "Digite a fonte:",
            lambda source: search_by_source(source)),
        "4": (
            "Digite a categoria:",
            lambda category: search_by_category(category)),
        "5": ("", lambda x: top_5_news()),
        "6": ("", lambda x: top_5_categories()),
        "7": ("Encerrando script",),
    }

    try:
        print(menu)
        user_option = input()

        print(menu_instruction[user_option][0])

        if user_option == "7":
            return

        user_data = input()
        print(menu_instruction[user_option][1](user_data))
        return

    except Exception:
        print("Opção inválida", file=sys.stderr)
