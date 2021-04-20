from rest_framework import generics
from ..models import Article, Country, Source
from .serializers import ArticleSerializer, CountrySerializer, SourceSerializer


class ArticleListView(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class CountryListView(generics.ListCreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class CountryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class SourceListView(generics.ListCreateAPIView):
    queryset = Source.objects.all()
    serializer_class = SourceSerializer


class SourceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Source.objects.all()
    serializer_class = SourceSerializer
