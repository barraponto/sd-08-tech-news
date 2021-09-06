from tech_news.database import get_collection


# Requisito 10
def top_5_news():
    top_5_list = list(get_collection().aggregate(
        [{"$addFields": {"interactions":
         {"$add": ["$comments_count", "$shares_count"]}}},
         {"$sort": {"interactions": -1, "title": 1}},
         {"$limit": 5},
         {"$project": {"title": 1, "url": 1, "_id": 0}}]))
    return [(el["title"], el["url"]) for el in top_5_list]


# Requisito 11
def top_5_categories():
    return [item["_id"] for item in list(get_collection().aggregate(
        [{"$unwind": "$categories"},
         {"$group": {"_id": "$categories", "amount": {"$sum": 1}}},
         {"$sort": {"amount": -1, "_id": 1}},
         {"$limit": 5},
         {"$project": {"_id": 1}}]))]
