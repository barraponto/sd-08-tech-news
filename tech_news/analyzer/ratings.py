from collections import Counter
from tech_news.database import find_news


def myFunc(e):
    if e["title"]:
        popularity = e["shares_count"] + e["comments_count"]
        return -popularity, e["title"]
    return 0, "ww"


# Requisito 10
def top_5_news():
    """Possível buscar as cinco top notícias; Possível buscar as cinco top
    notícias e retornar vazio caso não tenha nenhuma notícia; Caso houver
    menos de 5 notícias, serão retornadas quantas houverem"""

    news = find_news()
    news.sort(key=myFunc)
    return [(item["title"], item["url"]) for item in news[:5]]


# Requisito 11
def top_5_categories():
    """Possível buscar as cinco top categorias; Possível buscar as cinco top
    categorias e retornar vazio caso não tenha nenhuma notícia; Caso houver
    menos de 5 categorias, serão retornadas quantas houverem"""

    most_categories = Counter(
        sorted(
            [
                category_item
                for new_item in find_news()
                for category_item in new_item["categories"]
            ]
        )
    ).most_common()[:5]

    return [
        top_5_categories_list[0] for top_5_categories_list in most_categories
    ]
