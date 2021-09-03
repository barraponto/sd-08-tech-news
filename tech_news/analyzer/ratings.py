from tech_news.database import find_news
from operator import itemgetter


# Requisito 10
def top_5_news():
    news = []
    top_five = []
    search = find_news()
    for unity_new in search:
        popularity = unity_new["shares_count"] + unity_new["comments_count"]
        title_popularity = (unity_new["title"], popularity)
        news.append(title_popularity)

    sorted(news, key=itemgetter(2), reverse=True)
    for index in range(5):
        title_url = (news["title"][index], news["url"][index])
        top_five.append(title_url)
    return news


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
