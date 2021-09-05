from tech_news.database import db


# Requisito 10
def top_5_news():
    results = list(
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
                {"$limit": 5},
                {"$project": {"_id": 0, "url": 1, "title": 1}},
            ]
        )
    )
    return [(news["title"], news["url"]) for news in results]


# Requisito 11
def top_5_categories():
    results = list(
        db.news.aggregate(
            [
                {"$unwind": "$categories"},
                {"$group": {"_id": "$categories", "count": {"$sum": 1}}},
                {"$sort": {"_id": 1}},
                {"$limit": 5},
            ]
        )
    )
    return [(news["_id"]) for news in results]
