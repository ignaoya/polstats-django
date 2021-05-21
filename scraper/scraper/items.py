from scrapy_djangoitem import DjangoItem
from main_app.models import Article, Source, Country


class ArticleItem(DjangoItem):
    django_model = Article


class SourceItem(DjangoItem):
    django_model = Source


class CountryItem(DjangoItem):
    django_model = Country
