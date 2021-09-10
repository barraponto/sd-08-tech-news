from tech_news.database import find_news
import operator

# Requisito 10
def top_5_news():
    
    news = []
    result = find_news()
    
    for index in result:
        index["popularity"] = index["shares_count"] + index["comments_count"]

    # result.sort(key=operator.itemgetter("sum"), reverse=True)
    sorted_result = sorted(
        result, key=lambda news: news["popularity"],
        reverse=True
    )

    for index in sorted_result:
        news.append((index["title"], index["url"]))

    news_return = news[:5]
    return news_return



# Requisito 11
def top_5_categories():
    
    categories = []
    result = find_news()
    
    if len(result) > 0:
        for index in result:
            categories.extend(index["categories"])
    else:
        return []

    categories.sort()
    categories_return = categories[:5]
    
    return categories_return
