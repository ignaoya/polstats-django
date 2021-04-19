from rest_framework import generics
from ..models import Article, Country, Source
from .serializers import ArticleSerializer, CountrySerializer, SourceSerializer


class ArticleListView(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleDetailView(generics.RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class CountryListView(generics.ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class CountryDetailView(generics.RetrieveAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class SourceListView(generics.ListAPIView):
    queryset = Source.objects.all()
    serializer_class = SourceSerializer


class SourceDetailView(generics.RetrieveAPIView):
    queryset = Source.objects.all()
    serializer_class = SourceSerializer
