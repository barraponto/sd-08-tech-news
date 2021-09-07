from tech_news.database import find_news


# Requisito 10
def top_5_news():
    """Seu código deve vir aqui"""
    news = find_news()
    popularity_list = []
    result = []

    if len(news) > 0:
        for dic_news in news:
            popularity = dic_news["shares_count"] + dic_news["comments_count"]
            dic_news["popularity"] = popularity
            popularity_list.append(dic_news)
        # https://stackoverflow.com/questions/72899/how-do-i-sort-a-list-of-dictionaries-by-a-value-of-the-dictionary
        popularity_list.sort(
            key=lambda x: (x["popularity"], x["title"]), reverse=True)
        for news in popularity_list[:5]:
            result.append((news["title"], news["url"]))
        return result
    else:
        return []


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
