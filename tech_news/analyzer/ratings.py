from tech_news.database import find_news


# Requisito 10
def top_5_news():
    news = find_news()
    if len(news) == 0:
        return news
    top_news = []
    for new in news:
        top_news.append((
            new["shares_count"] + new["comments_count"],
            new['title'], new['url']
        ))
    news_sorted = sorted(top_news, key=lambda x: x[0], reverse=True)
    if len(news_sorted) < 5:
        n = len(news_sorted)
    else:
        n = 5
    top_five = []
    m = 0
    while n > 0:
        top_five.append((news_sorted[m][1], news_sorted[m][2]))
        n -= 1
        m += 1
        print(n)
    print(top_five)
    return top_five


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""


"""
    https://www.hashtagtreinamentos.com/funcoes-lambda-python?gclid=
    Cj0KCQjwm9yJBhDTARIsABKIcGbH4I8i4OseGDNaWNY8jP4AWzT8kAEHxYJqnvkf0B6PrRuCLyK6_bcaAtzEEALw_wcB
    https://www.kite.com/python/answers/how-to-sort-a-%60counter%60-object-by-count-in-python
    https://docs.python.org/pt-br/3/howto/sorting.html
    https://programadorviking.com.br/sorted-python-3-formas-incriveis-de-ordenar-listas-em-python/
"""
