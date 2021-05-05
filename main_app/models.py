from django.db import models
from datetime import date


class Country(models.Model):
    name = models.CharField(max_length=250)
    #articles = models.ManyToManyField(Article, related_name='article_countries')

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Source(models.Model):
    url = models.CharField(max_length=500)
    name = models.CharField(max_length=250)
    origin = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='country_sources')

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name + '-' + self.origin.name


class Article(models.Model):
    url = models.CharField(max_length=500)
    title = models.TextField()
    rating = models.IntegerField(default=0, blank=True, null=True)
    date = models.DateField(default=date.today, blank=True, null=True)
    length = models.IntegerField(default=0, blank=True, null=True)
    source = models.ForeignKey(Source, on_delete=models.CASCADE, related_name='source_articles', blank=True, null=True)
    countries = models.ManyToManyField(Country, related_name='country_articles')

    class Meta:
        ordering = ('-date',)

    def __str__(self):
        return self.title + '-' +  self.source.name






