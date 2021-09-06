import sys
from tech_news.scraper import get_tech_news
from tech_news.analyzer.search_engine import search_by_title, \
    search_by_date, search_by_source, search_by_category
from tech_news.analyzer.ratings import top_5_categories, top_5_news


main_msg = "Selecione uma das opções a seguir:\n\
 0 - Popular o banco com notícias;\n\
 1 - Buscar notícias por título;\n\
 2 - Buscar notícias por data;\n\
 3 - Buscar notícias por fonte;\n\
 4 - Buscar notícias por categoria;\n\
 5 - Listar top 5 notícias;\n\
 6 - Listar top 5 categorias;\n\
 7 - Sair."

err_option = "Opção inválida"


def populate_data():
    qty = input("Digite quantas notícias serão buscadas:")
    get_tech_news(qty)


def find_by_title():
    title = input("Digite o título:")
    result = search_by_title(title)
    print(result)


def find_by_date():
    date = input("Digite a data no formato aaaa-mm-dd:")
    result = search_by_date(date)
    print(result)


def find_by_source():
    source = input("Digite a fonte:")
    result = search_by_source(source)
    print(result)


def find_by_category():
    category = input("Digite a categoria:")
    result = search_by_category(category)
    print(result)


def show_top_5_news():
    print(top_5_news())


def show_top_5_categories():
    print(top_5_categories())


def end():
    print("Encerrando script")


def err():
    print(err_option, file=sys.stderr)


menu_flows = [populate_data, find_by_title, find_by_date,
              find_by_source, find_by_category, show_top_5_news,
              show_top_5_categories, end]


# Requisito 12
def analyzer_menu():
    try:
        option = input(main_msg)
        menu_flows[int(option)]()
    except IndexError:
        err()
    except ValueError:
        err()
