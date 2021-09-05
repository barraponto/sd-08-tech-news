import sys
from tech_news.scraper import get_tech_news
from tech_news.analyzer.search_engine import (
    search_by_title,
    search_by_date,
    search_by_source,
    search_by_category,
)
from tech_news.analyzer.ratings import top_5_news, top_5_categories


def executable_options():
    return {
        0: populate_database,
        1: get_by_title,
        2: get_by_date,
        3: get_by_source,
        4: get_by_category,
        5: top_5_news,
        6: top_5_categories,
    }


def populate_database():
    print("Digite quantas notícias serão buscadas:", end=" ")
    amount = int(input())
    get_tech_news(amount)
    print(f"Foram adicionada(s) {amount} notícia(s) no banco de dados")


def get_by_title():
    print("Digite o título:", end=" ")
    title = input()
    news_found = search_by_title(title)
    print(news_found)


def get_by_date():
    print("Digite a data no formato aaaa-mm-dd:", end=" ")
    date = input()
    try:
        news_found = search_by_date(date)
        print(news_found)
    except ValueError as err:
        print(err)


def get_by_source():
    print("Digite a fonte:", end=" ")
    source_name = input()
    news_found = search_by_source(source_name)
    print(news_found)


def get_by_category():
    print("Digite a categoria:", end=" ")
    category_name = input()
    news_found = search_by_category(category_name)
    print(news_found)


# Requisito 12
def analyzer_menu():
    """Seu código deve vir aqui"""
    print(
        "Selecione uma das opções a seguir:\n"
        " 0 - Popular o banco com notícias;\n"
        " 1 - Buscar notícias por título;\n"
        " 2 - Buscar notícias por data;\n"
        " 3 - Buscar notícias por fonte;\n"
        " 4 - Buscar notícias por categoria;\n"
        " 5 - Listar top 5 notícias;\n"
        " 6 - Listar top 5 categorias;\n"
        " 7 - Sair."
    )
    try:
        user_option = int(input())
        if user_option == 7:
            print("Encerrando script")
            return
        options = executable_options()
        options[user_option]()
    except Exception:
        return sys.stderr.write("Opção inválida\n")
