from django.test import TestCase
from ..models import Article, Source, Country


class CountryTest(TestCase):

    def setUp(self):
        Country.objects.create(name="Argentina")
        Country.objects.create(name="Hungary")

    def test_number_of_countries(self):
        countries = Country.objects.all()
        self.assertEqual(len(countries), 2)

    def test_names_of_countries(self):
        countries = Country.objects.all()
        self.assertEqual(countries[0].name, "Argentina")
        self.assertEqual(countries[1].name, "Hungary")
