from rest_framework import serializers
from ..models import Article, Country, Source


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['id', 'name']


class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = ['id', 'url', 'name', 'origin']


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'url', 'title', 'text', 'rating', 'date', 'length', 'source', 'countries']
