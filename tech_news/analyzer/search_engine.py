import re
from tech_news.database import find_news


# Requisito 6
def search_by_title(title):
    # search_list = search_news({{}, {'title': f'/ {title} /i'}})
    # objectiv = re.compile(title)
    search_list = find_news()
    list_news = []
    for item in search_list:
        print(re.search(title, item['title'], re.IGNORECASE))
        if re.search(title, item['title'], re.IGNORECASE):
            # print(item['title'], item['url'])
            result = (item['title'], item['url'])
            list_news.append(result)
    # list_s = [(item.title, item.url) for item in search_list]
    # print(objectiv.match(item['title']))
    return list_news
    """Seu código deve vir aqui"""


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
