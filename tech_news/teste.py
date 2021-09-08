from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    result = search_news({"title": {"$regex": title}})

    return result

