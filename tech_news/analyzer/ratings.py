from tech_news.database import find_news


def by_popularity(new):
    return new['shares_count'] + new['comments_count']


def format_output_new(idx, new):
    return (f'noticia_{idx}',  new['url'])


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
    """Seu código deve vir aqui"""
