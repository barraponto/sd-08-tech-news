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


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
