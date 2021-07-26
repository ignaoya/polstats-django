from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from ..models import Article, Source, Country
from django.contrib.auth.models import User


class CountryListTests(APITestCase):
    def setUp(self):
        Country.objects.create(name="Hungary")
        Country.objects.create(name="Argentina")
        
    def test_get_list_of_countries(self):
        url = reverse('api:country_list')
        data = {}
        response = self.client.get(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['name'], 'Argentina')
        self.assertEqual(response.data[1]['name'], 'Hungary')

    def test_post_create_new_country(self):
        url = reverse('api:country_list')
        data = {'name': 'Japan'}
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data['name'], 'Japan')

        response = self.client.get(url, {}, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)
        self.assertEqual(response.data[2]['name'], 'Japan')
