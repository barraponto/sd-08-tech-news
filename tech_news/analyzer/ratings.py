from tech_news.database import find_news

# Requisito 10


def top_5_news():
    top_five = []
    get_news = find_news()
    for item in get_news:
        item["popularity"] = item["comments_count"] + item["shares_count"]

    get_news = sorted(get_news, key=lambda x: x["title"])
    get_news = sorted(get_news, key=lambda x: x["popularity"], reverse=True)

    top_five = [
        get_news for get_news in get_news[:5]
    ]

    for item in top_five:
        top_five.append(tuple([item["title"], item["url"]]))

    return top_five


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
