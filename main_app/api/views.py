from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from ..models import Article, Country, Source
from .serializers import ArticleSerializer, CountrySerializer, SourceSerializer


class ArticleListView(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class ArticleDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class CountryListView(generics.ListCreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class CountryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class SourceListView(generics.ListCreateAPIView):
    queryset = Source.objects.all()
    serializer_class = SourceSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class SourceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Source.objects.all()
    serializer_class = SourceSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
