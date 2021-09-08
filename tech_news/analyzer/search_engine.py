from tech_news.database import search_news
from datetime import datetime


# Requisito 6
def search_by_title(title):
    """Seu código deve vir aqui"""
    # https://qastack.com.br/programming/1863399/mongodb-is-it-possible-to-make-a-case-insensitive-query
    # https://docs.mongodb.com/manual/reference/operator/query/regex/
    list_news = search_news({"title": {"$regex": title, "$options": "i"}})
    result_list = list()

    for each_news in list_news:
        result_list.append((each_news["title"], each_news["url"]))

    return result_list


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""
    # https://pt.stackoverflow.com/questions/377579/valida%C3%A7%C3%A3o-de-data-testes-com-python
    try:
        datetime.strptime(date, "%Y-%m-%d")
        list_news = search_news(
            {"timestamp": {"$regex": date}})
        result_list = list()

        for each_news in list_news:
            result_list.append((each_news["title"], each_news["url"]))

        return result_list
    except ValueError:
        raise ValueError('Data inválida')


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""
    list_news = search_news({"sources": {"$regex": source, "$options": "i"}})
    result_list = list()

    for each_news in list_news:
        result_list.append((each_news["title"], each_news["url"]))

    return result_list


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
    list_news = search_news(
        {"categories": {"$regex": category, "$options": "i"}})
    result_list = list()

    for each_news in list_news:
        print(each_news)
        result_list.append((each_news["title"], each_news["url"]))
        # print(result_list)

    return result_list
