import json
from rest_framework import status
from django.test import TestCase, Client, RequestFactory
from django.urls import reverse
from ..models import Article, Source, Country
from ..api.serializers import ArticleSerializer, SourceSerializer, CountrySerializer
from ..api.views import ArticleListView


client = Client()


class GetAllArticlesTest(TestCase):

    def setUp(self):
        self.hungary = Country.objects.create(name="Hungary")
        self.source = Source.objects.create(url='www.test.com',
                                            name='TestNews',
                                            origin=self.hungary)
        self.pos_story = Article.objects.create(url='www.test.com/positive_story',
                               title='Positive Story',
                               text='What a great story. Awesome!',
                               rating=10,
                               length=20,
                               source=self.source)
        self.neg_story = Article.objects.create(url='www.test.com/negative_story',
                               title='Negative Story',
                               text='What a bad story. Terrible!',
                               rating=-10,
                               length=20,
                               source=self.source)

    def test_get_valid_article_list(self):
        req = RequestFactory().get('/')
        response = ArticleListView.as_view()(req, *[], **{})
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
