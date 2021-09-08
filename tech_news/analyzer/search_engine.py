from tech_news.database import search_news
import re


# Requisito 6
def search_by_title(title):
    request_news = search_news({"title": {"$regex": title, "$options": "i"}})
    if len(request_news) > 0:
        return [(request_news[0]["title"], request_news[0]["url"])]
    else:
        return []


# Requisito 7
def search_by_date(date):
    year = date.split("-")[0]
    if int(year) < 2000 or len(year) != 4:
        raise ValueError("Data inválida")
    query = {"timestamp": {"$regex": f".*{date}.*"}}
    news_list = search_news(query)
    final_list = [(news["title"], news["url"]) for news in news_list]

    return final_list


# Requisito 8
def search_by_source(source):
    query = {"sources": {"$regex": re.compile(source, re.IGNORECASE)}}
    result = search_news(query)
    news_found = [(news["title"], news["url"]) for news in result]
    return news_found


# Requisito 9
def search_by_category(category):
    news = []
    rgx = re.compile(category, re.IGNORECASE)
    results = search_news({"categories": rgx})
    for result in results:
        news_tupla = (result["title"], result["url"])
        news.append(news_tupla)
    return news
