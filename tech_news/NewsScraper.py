from parsel import Selector


class NewsScraper:
    def __init__(self, html_content):
        self.selector = Selector(html_content)

    def get_news_urls(self):
        return self.selector.css(
            ".tec--list .tec--card__thumb__link::attr(href)"
        ).getall()

    def get_next_page_url(self):
        return self.selector.xpath(
            '//a[re:match(text(), "Mostrar mais notícias")]/@href'
        ).get()
