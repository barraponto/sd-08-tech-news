from tech_news.database import find_news


# Requisito 10
def top_5_news():
    """Seu código deve vir aqui"""


# Requisito 11
def top_5_categories():
    news_list = find_news()
    categories_result_list = []
    if len(news_list) > 0:
        for news in news_list:
            categories_result_list.extend(news["categories"])
    else:
        return []
    categories_result_list.sort()
    return categories_result_list[:5]
