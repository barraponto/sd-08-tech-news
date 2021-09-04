from parsel import Selector


class NewsDetailsScraper:
    def __init__(self, html_content):
        self.selector = Selector(html_content)

    def __get_url(self):
        return self.selector.css("link[rel=canonical]::attr(href)").get()

    def __get_title(self):
        return self.selector.css(".tec--article__header__title::text").get()

    def __get_timestamp(self):
        return self.selector.css(
            ".tec--timestamp__item time::attr(datetime)"
        ).get()

    def __get_writter(self):
        writer = self.selector.css(".tec--author__info__link::text").get()
        if not writer:
            writer = self.selector.css(
                ".tec--timestamp.tec--timestamp--lg a::text"
            ).get()
        if not writer:
            writer = self.selector.css(".tec--author__info p::text").get()
        return writer.strip() if writer else None

    def __get_shares_count(self):
        count = self.selector.css(".tec--toolbar").re_first(
            r"\d+ Compartilharam"
        )
        return int(count.split(" ")[0]) if count else 0

    def __get_comments_count(self):
        count = self.selector.css(".tec--toolbar").re_first(r"\d+ Comentários")
        return int(count.split(" ")[0]) if count else 0

    def __get_summary(self):
        return "".join(
            self.selector.css(
                ".tec--article__body > p:first-child *::text"
            ).getall()
        )

    def __get_sources(self):
        # trickie way
        # xpath_selector = (
        #     '//h2[re:match(text(), "Fontes")]/parent::div'
        #     '//a[contains(@class, "tec--badge")]/text()'
        # )
        # sources = self.selector.xpath(xpath_selector).getall()

        # easy way
        sources = self.selector.css(".z--mb-16.z--px-16 a::text").getall()
        if not sources:
            sources = self.selector.xpath(
                '//h2[re:match(text(), "Fontes")]/parent::div//a/text()'
            ).getall()
        return [source.strip() for source in sources]

    def __get_categories(self):
        categories = self.selector.css("#js-categories a::text").getall()
        return [categorie.strip() for categorie in categories]

    def render(self):
        result = {}
        result["url"] = self.__get_url()
        result["title"] = self.__get_title()
        result["timestamp"] = self.__get_timestamp()
        result["writer"] = self.__get_writter()
        result["shares_count"] = self.__get_shares_count()
        result["comments_count"] = self.__get_comments_count()
        result["summary"] = self.__get_summary()
        result["sources"] = self.__get_sources()
        result["categories"] = self.__get_categories()
        return result
