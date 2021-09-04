import sys
from tech_news.scraper import get_tech_news
from tech_news.analyzer.search_engine import (
    search_by_title,
    search_by_date,
    search_by_source,
    search_by_category,
)
from tech_news.analyzer.ratings import top_5_news, top_5_categories


def is_command(get_command):
    """Validate input for commands and cast it to int."""
    command = None
    try:
        command = int(get_command)
    except ValueError:
        error_message()

    return command


def error_message():
    sys.stderr.write("Opção inválida\n")


def exit_command():
    print("Encerrando script")


def arg_command(number, load):
    """Commands with arguments"""
    case = {
        0: get_tech_news,
        1: search_by_title,
        2: search_by_date,
        3: search_by_source,
        4: search_by_category,
    }
    return case[number](load)


def input_option(command):
    """Input options to get arguments for the command"""
    second_menu = {
        0: "Digite quantas notícias serão buscadas:",
        1: "Digite o título:",
        2: "Digite a data no formato aaaa-mm-dd:",
        3: "Digite a fonte:",
        4: "Digite a categoria:",
    }
    load = input(second_menu[command])
    response = ""
    if command == 0:
        response = is_command(load)
        if response is None:
            return None
    else:
        response = load

    return arg_command(command, response)


def analyzer_menu():
    """Command line aplication menu entry point"""
    menu = (
        "Selecione uma das opções a seguir:\n"
        " 0 - Popular o banco com notícias;\n"
        " 1 - Buscar notícias por título;\n"
        " 2 - Buscar notícias por data;\n"
        " 3 - Buscar notícias por fonte;\n"
        " 4 - Buscar notícias por categoria;\n"
        " 5 - Listar top 5 notícias;\n"
        " 6 - Listar top 5 categorias;\n"
        " 7 - Sair.\n"
    )
    get_command = input(menu)
    no_arg_commands = {5: top_5_news, 6: top_5_categories, 7: exit_command}
    command = is_command(get_command)
    if command is None:
        return None
    if 0 <= command <= 4:
        input_option(command)
    elif command <= 7:
        return no_arg_commands[command]()
    elif command > 7:
        error_message()
        return None
