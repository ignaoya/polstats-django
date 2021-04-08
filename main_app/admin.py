from django.contrib import admin
from .models import Article, Country, Source


# Register your models here.
admin.site.register(Article)
admin.site.register(Country)
admin.site.register(Source)

