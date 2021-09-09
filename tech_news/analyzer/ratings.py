from tech_news.database import db


# Requisito 10
def top_5_news():
    """Seu código deve vir aqui"""
    top_5 = list(
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

    return [(top["title"], top["url"]) for top in top_5]


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
