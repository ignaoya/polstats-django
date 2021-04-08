from django.db import models
from datetime import date

from django.db.models.deletion import CASCADE


class Country(models.Model):
    name = models.CharField(max_length=250)
    articles = models.ManyToManyField('Article', related_name='article_countries', through='CountryMentions')

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
    rating = models.IntegerField(default=0)
    date = models.DateField(default=date.today)
    length = models.IntegerField(default=0)
    source = models.ForeignKey(Source, on_delete=models.CASCADE, related_name='source_articles')
    countries = models.ManyToManyField('Country', related_name='country_articles', through='CountryMentions')

    class Meta:
        ordering = ('-date',)

    def __str__(self):
        return self.title + '-' +  self.source.name

class CountryMentions(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return "Article: " + str(self.article.id) + "Countries: " + str(self.country.id)





