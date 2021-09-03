from tech_news.database import find_news
from operator import itemgetter


# Requisito 10
def top_5_news():
    list_news = []
    search = find_news()
    if len(search) == 0:
        return search
    for unity_new in search:
        unity_new["popularity"] = int(unity_new["shares_count"]) + int(
            unity_new["comments_count"]
        )
        list_news.append(unity_new)
    top_five = sorted(
        list_news,
        key=itemgetter("popularity"),
        reverse=True,
    )[:5]
    return [(news["title"], news["url"]) for news in top_five]


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
