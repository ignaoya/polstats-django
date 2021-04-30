# Generated by Django 3.2 on 2021-04-28 13:17

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=500)),
                ('name', models.CharField(max_length=250)),
                ('origin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='country_sources', to='main_app.country')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=500)),
                ('title', models.TextField()),
                ('rating', models.IntegerField(default=0)),
                ('date', models.DateField(default=datetime.date.today)),
                ('length', models.IntegerField(default=0)),
                ('countries', models.ManyToManyField(related_name='country_articles', to='main_app.Country')),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='source_articles', to='main_app.source')),
            ],
            options={
                'ordering': ('-date',),
            },
        ),
    ]
