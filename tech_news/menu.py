import sys
import tech_news.scraper as scraper
import tech_news.analyzer.search_engine as search_engine
import tech_news.analyzer.ratings as ratings


def get_tech_news(number_of_news):
    scraper.get_tech_news(number_of_news)


def search_by_title(title):
    print(search_engine.search_by_title(title))


def search_by_date(date):
    print(search_engine.search_by_date(date))


def search_by_source(source):
    print(search_engine.search_by_source(source))


def search_by_category(category):
    print(search_engine.search_by_category(category))


def top_5_news():
    print(ratings.top_5_news())


def top_5_categories():
    print(ratings.top_5_categories())


def quit():
    print("Encerrando script")


# Requisito 12
def analyzer_menu():
    option = input(
        "Selecione uma das opções a seguir:\n"
        " 0 - Popular o banco com notícias;\n"
        " 1 - Buscar notícias por título;\n"
        " 2 - Buscar notícias por data;\n"
        " 3 - Buscar notícias por fonte;\n"
        " 4 - Buscar notícias por categoria;\n"
        " 5 - Listar top 5 notícias;\n"
        " 6 - Listar top 5 categorias;\n"
        " 7 - Sair.\n"
        "Opção: "
    )

    if option == "0":
        number_of_news = int(input("Digite quantas notícias serão buscadas: "))
        get_tech_news(number_of_news)
    elif option == "1":
        title = input("Digite o título: ")
        search_by_title(title)
    elif option == "2":
        date = input("Digite a data no formato aaaa-mm-dd: ")
        search_by_date(date)
    elif option == "3":
        source = input("Digite a fonte: ")
        search_by_source(source)
    elif option == "4":
        category = input("Digite a categoria: ")
        search_by_category(category)
    elif option == "5":
        top_5_news()
    elif option == "6":
        top_5_categories()
    elif option == "7":
        quit()
    else:
        print("Opção inválida", file=sys.stderr)
