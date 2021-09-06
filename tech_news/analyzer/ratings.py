from tech_news.database import find_news


# Requisito 10
def top_5_news():
    list = sorted(
            find_news(),
            key=lambda field: (
                -(field["shares_count"] + field["comments_count"]),
                field["title"],
            ),
        )[:5]
    return [(news["title"], news["url"]) for news in list]


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
