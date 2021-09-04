from tech_news.database import find_news


def by_popularity(new):
    return new['shares_count'] + new['comments_count']


def format_output_new(idx, new):
    return (f'noticia_{idx}',  new['url'])


def get_category_list(news):
    category_list = []

    for new in news:
        category_list = category_list + new['categories']

    return category_list


# Requisito 10
def top_5_news():
    news = find_news()
    news.sort(key=by_popularity, reverse=True)

    # http://devfuria.com.br/python/built-in-enumerate/
    return [
        format_output_new(idx, new)
        for idx, new in enumerate(news, start=1) if idx <= 5
    ]


# Requisito 11
def top_5_categories():
    news = find_news()

    category_list = get_category_list(news)
    category_list.sort()

    return [
        categorie
        for idx, categorie in enumerate(category_list, start=1) if idx <= 5
    ]
