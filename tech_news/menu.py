# Requisito 12
import sys
from tech_news.analyzer.ratings import top_5_categories, top_5_news
from tech_news.scraper import get_tech_news
from tech_news.analyzer.search_engine import (
    search_by_category,
    search_by_title,
    search_by_date,
    search_by_source,
)
from pprint import pprint


def views_format_news(list_news):
    for news in list_news:
        print("TITULO: ", news["title"])
        print("RESUMO DA NOTÍCIA: \n", news["summary"])
        print("URL:    ", news["url"])
        print("AUTOR(A) DA NOTÍCIA: ", news["writer"])
        print("DATA: ", news["timestamp"])
        print("NÚMERO DE COMPARTILHAMENTO: ", news["shares_count"])
        print("NÚMERO DE COMENTARIOS: ", news["comments_count"])
        print("FONTES DA NOTÍCIA:")
        (print(x, end="\n") for x in news["sources"])
        print("CATEGORIAS DA NOTÍCIA:")
        (print(x, end="\n") for x in news["categories"])
        print("\n")


def options_functions() -> dict:
    options = dict()
    options = {
        "0": get_tech_news,
        "1": search_by_title,
        "2": search_by_date,
        "3": search_by_source,
        "4": search_by_category,
        "5": top_5_news,
        "6": top_5_categories,
    }
    return options


def message() -> dict:
    options_msg = dict()
    options_msg = {
        "0": "Digite quantas notícias serão buscadas:",
        "1": "Digite o título:",
        "2": "Digite a data no formato aaaa-mm-dd:",
        "3": "Digite a fonte:",
        "4": "Digite a categoria:",
    }
    return options_msg


def switch_case(opc: str):
    options = options_functions()
    opc_msg = message()
    if opc == "0":
        value = input(opc_msg[opc])
        results = options[opc](value)
        views_format_news(results)

    elif opc_msg.get(opc) and int(opc) <= 4:
        value = input(opc_msg[opc])
        pprint(options[opc](value))

    elif opc == "7":
        return True

    elif options.get(opc):
        pprint(options[opc]())

    else:
        sys.stderr.write("Opção inválida\n")


def analyzer_menu():
    opc = ""
    EXIT = False

    while not EXIT:
        print(
            str(
                "Selecione uma das opções a seguir:\n "
                "0 - Popular o banco com notícias;\n "
                "1 - Buscar notícias por título;\n "
                "2 - Buscar notícias por data;\n "
                "3 - Buscar notícias por fonte;\n "
                "4 - Buscar notícias por categoria;\n "
                "5 - Listar top 5 notícias;\n "
                "6 - Listar top 5 categorias;\n "
                "7 - Sair."
            )
        )
        opc = str(input())
        EXIT = switch_case(opc)
        if EXIT:
            print("Encerrando script")
            break


if __name__ == "__main__":
    analyzer_menu()
