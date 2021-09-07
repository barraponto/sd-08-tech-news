from tech_news.database import find_news


# Requisito 10
def top_5_news():
    """Seu código deve vir aqui"""


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
    news = find_news()
    list_categories = []
    count_categories = []
    result = []
    for dic_news in news:
        list_categories.extend(dic_news["categories"])
    for item in list_categories:
        contador = list_categories.count(item)
        dict_count = {"item": item, "count": contador}
        if dict_count not in count_categories:
            count_categories.append(dict_count)
    count_categories.sort(key=lambda x: (x["count"], x["item"]))
    for item in count_categories[:5]:
        result.append(item["item"])
    return result
