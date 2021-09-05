from collections import Counter
import tech_news.database as db


# Requisito 10
def top_5_news():
    """Seu código deve vir aqui"""
    found_news = db.find_news()
    news_popularity = [
        {
            "title": new["title"],
            "url": new["url"],
            "popularity": new["comments_count"] + new["shares_count"],
        }
        for new in found_news
    ]
    sorted_news_by_popularity = sorted(
        news_popularity, key=lambda news: news["popularity"],
        reverse=True
    )
    most_popular_news = sorted_news_by_popularity[:5]
    return [(new['title'], new['url']) for new in most_popular_news]


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
    found_news = db.find_news()
    news_categories = [
        category
        for news in found_news
        for category in news["categories"]
    ]
    sorted_categories = sorted(news_categories, key=lambda news: news.lower())
    most_appearences_categories = Counter(sorted_categories).most_common()
    return [category[0] for category in most_appearences_categories][:5]
