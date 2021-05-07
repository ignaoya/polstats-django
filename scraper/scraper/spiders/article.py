from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scraper.items import ArticleItem


class ArticleSpider(CrawlSpider):
    name = 'article'
    allowed_domains = ['www.rt.com']
    start_urls = ['https://www.rt.com']
    rules = [
        Rule(LinkExtractor(allow='(/op-ed/).*'),
            callback='parse_items', follow=True),
    ]

    # Page count limit to avoid over-scraping and getting banned while in development
    COUNT_MAX = 5
    custom_settings = {
        'CLOSESPIDER_PAGECOUNT': COUNT_MAX
    }

    def parse_items(self, response):
        article = ArticleItem()
        divs = response.xpath('//div')
        article["url"] = response.url
        article["title"] = response.css('h1::text').extract_first()
        article["text"] = ''.join(divs.xpath('.//p').extract())
        return article
