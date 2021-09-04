from datetime import datetime
import re

from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    results = search_news({"title": {"$regex": f"{title}", "$options": "i"}})
    return [(result["title"], result["url"])
            for result in results]


# Requisito 7
def search_by_date(date):

    valid_date_format = re.compile(
        '^20[0-2][0-9]-((0[1-9])|(1[0-2]))-([0-2][1-9]|3[0-1])$')

    if not valid_date_format.match(date):
        raise ValueError("Data inválida")
    else:
        date_string_list = date.split('-')
        date_int_list = [int(element) for element in date_string_list]
        start = datetime.isoformat(datetime(*date_int_list))
        end = datetime.isoformat(datetime(*date_int_list, 23, 59))

        results = search_news({"timestamp": {"$gte": start, "$lte": end}})
        return [(result["title"], result["url"])
                for result in results]


# Requisito 8
def search_by_source(source):
    results = search_news(
        {"sources": {"$elemMatch": {"$regex": f"{source}", "$options": "i"}}})
    return [(result["title"], result["url"])
            for result in results]


# Requisito 9
def search_by_category(category):
    results = search_news({
        "categories": {
            "$elemMatch": {
                "$regex": f"{category}", "$options": "i"
                }
            }
        })
    return [(result["title"], result["url"])
            for result in results]
