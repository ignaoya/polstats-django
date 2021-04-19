from django.contrib import admin
from .models import Article, Country, Source


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['url', 'title', 'date']


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Source)
class SourceAdmin(admin.ModelAdmin):
    list_display = ['url', 'name', 'origin']

