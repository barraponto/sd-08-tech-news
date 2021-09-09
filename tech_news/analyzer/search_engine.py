from tech_news.database import search_news
import datetime


# Requisito 6
def search_by_title(title):
    """Seu código deve vir aqui"""
    # $regex- Fornece recursos de expressão regular para strings
    # de correspondência de padrões em consultas. O MongoDB usa
    # expressões regulares compatíveis com Perl (ou seja, "PCRE")
    # versão 8.42 com suporte a UTF-8.
    # fonte: docs.mongodb.com/manual/reference/operator/query/regex/
    # $option: "i" Perform Case-Insensitive Regular Expression Match
    title_regex = {"title": {"$regex": title, "$options": "i"}}
    search_title_list = search_news(title_regex)
    return [(new["title"], new["url"]) for new in search_title_list]


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""
    try:
        format_date = "%Y-%m-%d"
        datetime.datetime.strptime(date, format_date)
        regex_date = {"timestamp": {"$regex": date}}
        search_list_date = search_news(regex_date)
        return [(new["title"], new["url"]) for new in search_list_date]
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
