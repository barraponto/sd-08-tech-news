from parsel import Selector


class GetScrapeNoticia:
    def __init__(self, html_content):
        self.selector = Selector(html_content)

    def get_url(self):
        return self.selector.css("link[rel=canonical]::attr(href)").get()

    def get_title(self):
        return self.selector.css(".tec--article__header__title::text").get()

    def get_timestamp(self):
        return self.selector.css(
            ".tec--timestamp__item time::attr(datetime)"
        ).get()

    def get_writer(self):
        writer = self.selector.css(".tec--author__info__link::text").get()
        if not writer:
            return None
        return writer.strip()

    def get_shares_count(self):
        shares_count = self.selector.css(".tec--toolbar__item::text").get()
        if not shares_count:
            return 0
        # https://pt.stackoverflow.com/a/254909
        return int(
            "".join(number for number in shares_count if number.isdigit())
        )

    def get_comments_count(self):
        comments_count = self.selector.css(".tec--btn::attr(data-count)").get()
        if not comments_count:
            return 0
        return int(comments_count)

    def get_summary(self):
        return "".join(
            self.selector.css(
                ".tec--article__body > p:first-child *::text"
            ).getall()
        )

    def get_sources(self):
        sources = self.selector.css(".z--mb-16.z--px-16 a::text").getall()
        return [source.strip() for source in sources]

    def get_categories(self):
        categories = self.selector.css(
            ".z--px-16 > #js-categories a::text"
        ).getall()
        return [category.strip() for category in categories]

    def news_dictionary(self):
        new_dict = dict()
        new_dict["url"] = self.get_url()
        new_dict["title"] = self.get_title()
        new_dict["timestamp"] = self.get_timestamp()
        new_dict["writer"] = self.get_writer()
        new_dict["shares_count"] = self.get_shares_count()
        new_dict["comments_count"] = self.get_comments_count()
        new_dict["summary"] = self.get_summary()
        new_dict["sources"] = self.get_sources()
        new_dict["categories"] = self.get_categories()
        return new_dict


# print(GetScrapeNoticia(html_content))
