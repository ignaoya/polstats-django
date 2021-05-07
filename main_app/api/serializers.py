from rest_framework import serializers
from ..models import Article, Country, Source


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['name']


class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = ['url', 'name', 'origin']


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['url', 'title', 'text', 'rating', 'date', 'length', 'source', 'countries']
