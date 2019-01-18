import scrapy

class HackerNewsSpider(scrapy.Spider):
    name = 'hacker_news'
    # start on new stories page
    start_urls = ['https://news.ycombinator.com/newest']
    # HN has an aggressive block policy
    custom_settings = {
        'DOWNLOAD_DELAY': 30,
        'CONCURRENT_REQUESTS_PER_DOMAIN': 1,
        'AUTOTHROTTLE_ENABLED': True,
    }

    def parse(self, response):
        for username in response.css('a.hnuser'):
            yield {'username': username.css('a ::text').extract_first()}

        # follow "More" link on new stories list
        for next_page in response.css('a.morelink'):
            yield response.follow(next_page, self.parse)

        # follow stories with comments
        for story_td in response.css('td.subtext'):
            story_link = story_td.css('a:nth-child(8)')
            if story_link.css('::text').extract_first() != 'discuss':
                yield response.follow(story_link[0], self.parse)
