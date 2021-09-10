use('tech_news')

db.news.find({})
aggregate(
  [{'$project': {
      "title": 1,
      "url": 1,
      "timestamp": {'$substr': ["2019-12-12", 0, 2]}
  }
  }])