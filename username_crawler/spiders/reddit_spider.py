import scrapy

class RedditSpider(scrapy.Spider):
    name = 'reddit'
    custom_settings = {
        'ROBOTSTXT_OBEY': False,
    }
    start_urls = ['https://old.reddit.com/']

    def parse(self, response):
        for username in response.css('a.author'):
            yield {'username': username.css('a ::text').extract_first()}

        # follow comments links
        for comment_page in response.css('a.comments'):
            yield response.follow(comment_page, self.parse)

        # follow "next" button on main page
        for next_page in response.css('span.next-button a.next'):
            yield response.follow(next_page, self.parse)
