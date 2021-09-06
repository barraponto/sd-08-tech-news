from tech_news.database import find_news


# Requisito 10
def top_5_news():
    get_news = find_news()
    popularity_list = [
        {
            "title": new["title"],
            "popularity": new["shares_count"] + new["comments_count"],
            "url": new["url"],
        }
        for new in get_news
    ]
    # ordenando do maior para o menor no parâmetro "popularity"
    # i["popularity"]
    # limitando em 5 resultados
    # [:5]
    limit_list = sorted(
        popularity_list, key=lambda i: (i["popularity"]), reverse=True
    )[:5]
    # https://docs.python.org/pt-br/3.7/howto/sorting.html
    return [(new["title"], new["url"]) for new in limit_list]


# Requisito 11
def top_5_categories():
    get_news = find_news()
    if get_news is None:
        return []
    categories_list = [{"categories": new["categories"]} for new in get_news]
    categories1 = list(map(lambda new: new["categories"][0], categories_list))
    categories2 = list(map(lambda new: new["categories"][1], categories_list))
    if len(get_news) < 5:
        console = categories2[:2]
        pc = categories1[:2]
        console.extend(pc)
        return console
    return categories2[:5]
