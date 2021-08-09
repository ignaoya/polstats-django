import pycountry
from django.db import models
from datetime import date


class Country(models.Model):
    name = models.CharField(max_length=250)

    class Meta:
        ordering = ('name',)

    def __str__(self) -> str:
        return self.name


class Source(models.Model):
    url = models.CharField(max_length=500)
    name = models.CharField(max_length=250)
    origin = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='country_sources')

    class Meta:
        ordering = ('name',)

    def __str__(self) -> str:
        return self.name + '-' + self.origin.name


class Article(models.Model):
    url = models.CharField(max_length=500, unique=True)
    title = models.TextField()
    text = models.TextField(blank=True, null=True)
    rating = models.IntegerField(default=0, blank=True, null=True)
    date = models.DateField(default=date.today, blank=True, null=True)
    length = models.IntegerField(default=0, blank=True, null=True)
    source = models.ForeignKey(Source, on_delete=models.CASCADE, related_name='source_articles', blank=True, null=True)
    countries = models.ManyToManyField(Country, related_name='country_articles')

    class Meta:
        ordering = ('-date',)

    def __str__(self) -> str:
        return self.title + '-' +  self.source.name

    def get_countries(self) -> None:
        countries = []
        for country in pycountry.countries:
            if country.name in self.text:
                new_country = Country.objects.filter(name=country.name)
                if new_country:
                    new_country = new_country[0]
                else:
                    new_country = Country(name=country.name)
                    new_country.save()
                countries.append(new_country)
        self.countries.add(*countries)
        self.save()







