from tech_news.database import search_news

# import time
# import datetime

# import json
# from parsel import Selector
# import re

SOUCE = "RESETERA"

data = search_news({"sources": {"$regex": f"^(?i){SOUCE}"}})


print(len(data))
