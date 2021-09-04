from tech_news.database import search_news
from datetime import datetime


def format_news(new):
    return (new['title'], new['url'])


def is_valid_date(date):
    try:
        # https://www.alura.com.br/artigos/lidando-com-datas-e-horarios-no-python?gclid=Cj0KCQjwssyJBhDXARIsAK98ITRxkPnQnvWJoiebq-w-4ErT4HX-gL8qLA6jD7hG9N7sXox8TKfkqv0aAjczEALw_wcB
        datetime.strptime(date, "%Y-%m-%d")
        return True
    except ValueError:
        return False


# Requisito 6
def search_by_title(title):
    # https://docs.mongodb.com/manual/reference/operator/query/regex/
    query = {'title': {'$regex': f'.*{title}.*', '$options': "i"}}
    news = search_news(query)

    return [format_news(new) for new in news]


# Requisito 7
def search_by_date(date):
    if is_valid_date(date) is False:
        raise ValueError("Data inválida")
    else:
        # https://docs.mongodb.com/manual/reference/operator/query/regex/
        search_news_query = {"timestamp": {"$regex": date, "$options": "i"}}
        news = search_news(search_news_query)

        return [format_news(new) for new in news]


# Requisito 8
def search_by_source(source):
    seach_query = {'sources': {'$regex': f'.*{source}.*', '$options': "i"}}
    news = search_news(seach_query)

    return [format_news(new) for new in news]


# Requisito 9
def search_by_category(category):
    query = {'categories': {'$regex': f'.*{category}.*', '$options': "i"}}
    news = search_news(query)

    return [format_news(new) for new in news]
