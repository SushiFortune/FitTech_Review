import scrapy

class PcmagSpider(scrapy.Spider):
    name = 'pcmag_spider'
    allowed_domains = ['pcmag.com']
    start_urls = ['https://www.pcmag.com/reviews/fitbit-sense-2']

    def parse(self, response):
        review_number = response.css('.review-count::text').get()
        yield {
            'review_number': review_number
        }

