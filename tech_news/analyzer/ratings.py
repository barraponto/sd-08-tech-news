from tech_news.database import find_news


def get_popularity(item):
    return item['popularity']


# Requisito 10
def top_5_news():
    search_list = find_news()
    list_news = []
    for item in search_list:
        result = {
            "title": item["title"],
            "url": item["url"],
            "popularity": int(
                int(item["shares_count"]) + int(item["comments_count"])
            ),
        }
        list_news.append(result)
    list_news.sort(key=get_popularity, reverse=True)
    ordered_list = []
    for item in list_news[:5]:
        result = (item["title"], item["url"])
        ordered_list.append(result)
    return ordered_list
    """Seu código deve vir aqui"""


def get_categories_values(categories):
    return categories[1]


def get_categories_name(categories):
    return categories[0]


# Requisito 11
def top_5_categories():
    search_list = find_news()
    categories = {}
    for item in search_list:
        for category in item["categories"]:
            try:
                categories[category] = 1
            except KeyError:
                categories.update({category: 1})
            else:
                categories[category] += 1
    list_news = list(categories.items())
    list_news.sort(key=get_categories_name)
    list_news.sort(key=get_categories_values, reverse=True)
    ordered_list = []
    for item in list_news[:5]:
        ordered_list.append(item[0])
    print(ordered_list)
    return ordered_list
    """Seu código deve vir aqui"""
