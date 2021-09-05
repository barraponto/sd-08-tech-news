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
    """Seu código deve vir aqui"""
