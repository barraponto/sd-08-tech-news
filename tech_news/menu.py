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


def get_option():
    return input(
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


questions = {
    "0": "Digite quantas notícias serão buscadas: ",
    "1": "Digite o título: ",
    "2": "Digite a data no formato aaaa-mm-dd: ",
    "3": "Digite a fonte: ",
    "4": "Digite a categoria: ",
}

# Normalmente não seria necessário fazer essa gambiarra
# porém nos testes está havendo um patch e as funções
# que estavam sendo armazenadas no dicionário estavam
# mantendo suas versões originais, então estou usando uma
# lambda function para pegar a função em real time, aparentemente
# isso resolve o problema. Certamente deve haver
# uma forma melhor de fazer isso, mas como não posso mexer nos testes
# vai ficar assim mesmo.
options = {
    "0": lambda user_input: get_tech_news(user_input),
    "1": lambda user_input: search_by_title(user_input),
    "2": lambda user_input: search_by_date(user_input),
    "3": lambda user_input: search_by_source(user_input),
    "4": lambda user_input: search_by_category(user_input),
    "5": lambda: top_5_news(),
    "6": lambda: top_5_categories(),
    "7": lambda: quit(),
}


# Requisito 12
def analyzer_menu():
    option = get_option()

    try:
        if option in questions:
            user_answer = input(questions[option])
            options[option](user_answer)
        else:
            options[option]()
    except KeyError:
        print("Opção inválida", file=sys.stderr)
