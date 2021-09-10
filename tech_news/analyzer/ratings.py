from tech_news.database import db


# Requisito 10
def top_5_news():
    list_results = list(
        db.news.aggregate(
            [
                {
                    "$addFields": {
                        "popularidade": {
                            "$sum": ["$shares_count", "$comments_count"]
                        },
                    },
                },
                {"$sort": {"popularidade": -1}},
                {"$limit": 5},
                {"$project": {"_id": 0, "url": 1, "title": 1}},
            ],
        ),
    )

    return [(news["title"], news["url"]) for news in list_results]


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
