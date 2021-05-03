from scrapy_djangoitem import DjangoItem
from main_app.models import Article


class ArticleItem(DjangoItem):
    django_model = Article
