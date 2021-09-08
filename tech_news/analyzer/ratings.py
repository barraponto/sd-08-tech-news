from tech_news.database import find_news


# Requisito 10
def top_5_news():
    news = find_news()
    top_news = []
    for new in news:
        top_news = top_news.append(
            new["shares_count"] + news["comments_count"],
            news['title'], news['url']
        )
        top_five = sorted(top_news)
    return top_five[:5]


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
