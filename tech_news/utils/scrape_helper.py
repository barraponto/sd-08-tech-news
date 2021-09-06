from parsel import Selector


def scrape_news_writer(html_content):
    selector = Selector(text=html_content)

    try:
        writer = selector.css('.tec--author__info__link::text').get()
        return writer.strip()
    except AttributeError:
        return None


def scrape_news_shares_count(html_content):
    selector = Selector(html_content)

    try:
        shares_count = selector.css('.tec--toolbar__item::text').get()
        return int(shares_count.strip().split(' ')[0])
    except AttributeError:
        return 0

def scrape_news_comments_count(html_content):
    selector = Selector(html_content)

    try:
        comments_count = selector.css('#js-comments-btn::attr(data-count)').get()
        return int(comments_count.strip().split(' ')[0])
    except AttributeError:
        return 0
