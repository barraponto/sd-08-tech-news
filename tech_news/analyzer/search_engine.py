import re
import datetime
from tech_news.database import db


# https://stackoverflow.com/questions/6266555/querying-mongodb-via-pymongo-in-case-insensitive-efficiently

def search_by_title(title):
    news_response = db.news.find({
        'title': {'$regex': re.compile(title, re.IGNORECASE)}
    })

    return [(news['title'], news['url']) for news in news_response]


def search_by_date(date):
    try:
        datetime.datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        raise ValueError('Data inválida')

    news_response = db.news.find({
        'timestamp': {'$regex': re.compile(date)}
    })

    return [(news['title'], news['url']) for news in news_response]


def search_by_source(source):
    news_response = db.news.find({
        'sources': {'$regex': re.compile(source, re.IGNORECASE)}
    })

    return [(news['title'], news['url']) for news in news_response]


def search_by_category(category):
    news_response = db.news.find({
        'categories': {'$regex': re.compile(category, re.IGNORECASE)}
    })

    return [(news['title'], news['url']) for news in news_response]
