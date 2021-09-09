from tech_news.database import find_news
from operator import itemgetter


# Requisito 10
def top_5_news():
    """Seu código deve vir aqui"""
    # https://docs.python.org/pt-br/dev/howto/sorting.html
    list_news = find_news()
    news_populary = list()

    for each_news in list_news:
        data = (
            each_news["title"],
            each_news["url"],
            each_news["shares_count"] + each_news["comments_count"])
        news_populary.append(data)

    ranking_top_5 = sorted(
        news_populary,
        key=itemgetter(1, 2))

    list_ranking = []

    for ranking in ranking_top_5[:5]:
        ranking_print = (ranking[0], ranking[1])
        list_ranking.append(ranking_print)
    return list_ranking


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
