import re
from tech_news.database import find_news


# Requisito 6
def search_by_title(title):
    search_list = find_news()
    list_news = []
    for item in search_list:
        # https://stackoverflow.com/questions/6579876/how-to-match-a-substring-in-a-string-ignoring-case
        if re.search(title, item["title"], re.IGNORECASE):
            result = (item["title"], item["url"])
            list_news.append(result)
    return list_news


# Requisito 7
def search_by_date(date):
    if (
        # not re.search("\d{4}-\d{2}-\d{2}", date, re.IGNORECASE)
        int(date.split("-")[0]) < 2000
    ):
        raise ValueError("Data inválida")
    search_list = find_news()
    list_news = []
    for item in search_list:
        print(re.search(date, item["timestamp"], re.IGNORECASE))
        if re.search(date, item["timestamp"], re.IGNORECASE):
            result = (item["title"], item["url"])
            list_news.append(result)
    return list_news


# Requisito 8
def search_by_source(source):
    search_list = find_news()
    list_news = []
    for item in search_list:
        print(item['sources'])
        # https://stackoverflow.com/questions/6579876/how-to-match-a-substring-in-a-string-ignoring-case
        for soc in item['sources']:
            if re.search(source, soc, re.IGNORECASE):
                result = (item["title"], item["url"])
                list_news.append(result)
    return list_news


# Requisito 9
def search_by_category(category):
    search_list = find_news()
    list_news = []
    for item in search_list:
        print(item['sources'])
        # https://stackoverflow.com/questions/6579876/how-to-match-a-substring-in-a-string-ignoring-case
        for cat in item['categories']:
            if re.search(category, cat, re.IGNORECASE):
                result = (item["title"], item["url"])
                list_news.append(result)
    return list_news
    """Seu código deve vir aqui"""
