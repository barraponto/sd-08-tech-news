from tech_news.database import find_news
from collections import Counter
import itertools


# Requisito 10
def top_5_news():
    """Seu código deve vir aqui"""


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
    responses = find_news()
    categories_list = []
    for response in responses:
        categories_list.append(response["categories"])
    totals = Counter(
        i for i in list(itertools.chain.from_iterable(categories_list))
    )
    totals_sorted = sorted(totals)
    limit = slice(5)
    return totals_sorted[limit]
