from collections import Counter
from tech_news.database import db, find_news


# Requisito 10
def top_5_news():
    results = db.news.aggregate([
        {
            "$project": {
                "title": 1, "url": 1, "popularity": {
                    "$add": ["$shares_count", "$comments_count"]
                    }
                }
        },
        {
            "$sort": {"popularity": -1, "title": 1}
        },
        {
            "$limit": 5
        }

    ])

    return [(result["title"], result["url"])
            for result in list(results)]


# Requisito 11
def top_5_categories():
    results = find_news()
    categories = []
    for result in results:
        categories = [*categories, *result["categories"]]
    categories.sort()
    occcurrences = Counter(categories).most_common(5)

    return [category[0] for category in occcurrences]
