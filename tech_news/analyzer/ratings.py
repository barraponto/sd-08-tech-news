from tech_news.database import db


# Requisito 10
def search_top_news(qtd):
    return list(
        db.news.aggregate(
            [
                {
                    "$addFields": {
                        "popularity": {
                            "$sum": ["$shares_count", "$comments_count"]
                        }
                    }
                },
                {"$sort": {"popularity": -1}},
                {"$limit": qtd},
                {"$project": {"_id": 0, "url": 1, "title": 1}},
            ]
        )
    )


def top_5_news():
    return [(news["title"], news["url"]) for news in search_top_news(5)]


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
