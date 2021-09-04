from parsel import Selector


class NewsScraper:
    def __init__(self, html_content):
        self.selector = Selector(html_content)

    def get_news_urls(self):
        return self.selector.css(
            ".tec--list .tec--card__thumb__link::attr(href)"
        ).getall()
