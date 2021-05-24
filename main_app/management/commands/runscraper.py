from django.core.management.base import BaseCommand, CommandError
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from scraper.scraper.spiders.article import RTArticleSpider
from scraper.scraper import settings, pipelines, middlewares
from main_app.models import Article


class Command(BaseCommand):
    help = 'Runs the scraper'

    def handle(self, *args, **kwargs):
        process = CrawlerProcess(get_project_settings())
        process.crawl(RTArticleSpider)
        process.start()

