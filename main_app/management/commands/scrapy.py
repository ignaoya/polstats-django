from django.core.management.base import BaseCommand
from scrapy.cmdline import execute


class Command(BaseCommand):
    help = 'Runs the scraper'

    def handle(self, *args, **kwargs) -> None:
        args = ['scrapy', 'runspider', 'scraper/scraper/spiders/article.py']
        execute(args)

