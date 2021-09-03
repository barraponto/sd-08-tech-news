from tech_news.database import find_news

# from tech_news.analyzer.search_engine import serialize_news_list


# Requisito 10
def top_5_news():
    """Seu código deve vir aqui"""
    all_news = find_news()
    if not all_news:
        return []
    news_rates = [
        (
            news["shares_count"] + news["comments_count"],
            news["title"],
            news["url"],
        )
        for news in all_news
    ]
    news_rates.sort(key=lambda news: (news[0], news[1]), reverse=True)
    result = []
    for news in news_rates[:5]:
        result.append((news[1], news[2]))
    return result


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
    all_news = find_news()
    if not all_news:
        return []
    all_categories = {}

    for news in all_news:
        for category in news["categories"]:
            if category in all_categories:
                all_categories[category] += 1
            else:
                all_categories[category] = 1

    sorted_categories = list(all_categories.items())
    sorted_categories.sort(key=lambda category: category[0])
    sorted_categories.sort(key=lambda category: category[1], reverse=True)
    sorted_list = [category[0] for category in sorted_categories]
    return sorted_list[:5]
