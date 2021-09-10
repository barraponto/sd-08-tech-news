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
    return top_five


# Requisito 11
def top_5_categories():
    categories = []
    news = find_news()
    if len(news) == 0:
        return []
    for new in news:
        categories += (new['categories'])
    print(categories)
    sorted_categories = sorted(categories)
    return sorted_categories[:5]
