from tech_news.database import find_news


# Requisito 10
# https://stackoverflow.com/questions/72899/how-do-i-sort-a-list-of-dictionaries-by-a-value-of-the-dictionary
def top_5_news():
    news_list = []
    search = find_news()
    if len(search) == 0:
        return search
    for unity_new in search:
        unity_new["popularity"] = int(unity_new["shares_count"]) + int(
            unity_new["comments_count"]
        )
        news_list.append(unity_new)

    top_five = sorted(
        news_list,
        key=lambda curr_key: (curr_key["title"], curr_key["popularity"]),
    )[:5]
    return [(news["title"], news["url"]) for news in top_five]


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
