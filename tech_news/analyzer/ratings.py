from tech_news.database import find_news


# Requisito 10
def top_5_news():
    """Seu código deve vir aqui"""
    news_list = find_news()
    if len(news_list) == 0:
        return news_list
    top_new_list = []
    for new in news_list:
        top_new_list.append((
            new["shares_count"] + new["comments_count"],
            new['title'], new['url']
        ))
    # fonte: https://docs.python.org/pt-br/3.7/howto/sorting.html
    news_sorted = sorted(top_new_list, key=lambda x: x[0], reverse=True)
    if len(news_sorted) < 5:
        existent_news = len(news_sorted)
    else:
        existent_news = 5
    top_five = []
    m = 0
    while existent_news > 0:
        top_five.append((news_sorted[m][1], news_sorted[m][2]))
        existent_news -= 1
        m += 1

    return top_five
# referência: Aluna Rita Jeveax


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
