import sys
from tech_news.constants import NUM_MAX_OPTIONS
from tech_news.scraper import get_tech_news
from tech_news.analyzer.ratings import top_5_news, top_5_categories
from tech_news.analyzer.search_engine import (
    search_by_title,
    search_by_date,
    search_by_source,
    search_by_category,
)


def option_0(option):
    if option == "0":
        qty_news = int(input("Digite quantas notícias serão buscadas: "))
        print(get_tech_news(qty_news))


def option_1(option):
    if option == "1":
        title = input("Digite o título: ")
        print(search_by_title(title))


def option_2(option):
    if option == "2":
        date = input("Digite a data no formato aaaa-mm-dd: ")
        print(search_by_date(date))


def option_3(option):
    if option == "3":
        source = input("Digite a fonte: ")
        print(search_by_source(source))


def option_4(option):
    if option == "4":
        category = input("Digite a categoria: ")
        print(search_by_category(category))


def option_5(option):
    if option == "5":
        print(top_5_news())


def option_6(option):
    if option == "6":
        print(top_5_categories())


def option_7(option):
    if option == "7":
        print("Encerrando script")


# Requisito 12
def analyzer_menu():
    print(
        "Selecione uma das opções a seguir:\n",
        "0 - Popular o banco com notícias;\n",
        "1 - Buscar notícias por título;\n",
        "2 - Buscar notícias por data;\n",
        "3 - Buscar notícias por fonte;\n",
        "4 - Buscar notícias por categoria;\n",
        "5 - Listar top 5 notícias;\n",
        "6 - Listar top 5 categorias;\n",
        "7 - Sair.",
    )

    option = input()

    if (option.isdecimal() and
       int(option) >= 0 and int(option) <= NUM_MAX_OPTIONS):
        option_0(option)
        option_1(option)
        option_2(option)
        option_3(option)
        option_4(option)
        option_5(option)
        option_6(option)
        option_7(option)
    else:
        sys.stderr.write("Opção inválida\n")
