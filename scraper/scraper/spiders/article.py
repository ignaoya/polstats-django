from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scraper.items import ArticleItem
from sentiment.sentiment_analyzer import get_article_sentiment
from main_app.models import Source, Country

class RTArticleSpider(CrawlSpider):
    name = 'RTarticle'
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
        source = Source.objects.filter(name='RT')
        if source:
            source = source[0]
        else:
            country = Country.objects.filter(name='Russia')
            if country:
                country = country[0]
            else:
                country = Country(name='Russia')
                country.save()
            source = Source(url="www.rt.com", 
                            name="RT",
                            origin=country)
            source.save()
        article = ArticleItem()
        divs = response.xpath('//div')
        article["url"] = response.url
        article["title"] = response.css('h1::text').extract_first()
        article["text"] = ''.join(divs.xpath('.//p').extract())
        article["rating"] = get_article_sentiment(article["text"])
        article["length"] = len(article["text"])
        article["source"] = source
        return article
