    print(len(list_news))
    scrape_novi = scrape_novidades(fetch(page))
    print(scrape_novi)
    for each_news in scrape_novi:
        list_news.append(scrape_noticia(fetch(each_news)))
        print(list_news)
        page = scrape_next_page_link(fetch(page))
        print(page)
        if amount == len(list_news):
            # create_news(list_news)
            return list_news