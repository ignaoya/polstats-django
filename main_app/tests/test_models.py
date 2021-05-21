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


class SourceTest(TestCase):

    def setUp(self):
        country = Country.objects.create(name="Argentina")
        data = {'url': 'www.test.com', 
                'name': 'TestNews', 
                'origin': country}
        Source.objects.create(url=data['url'], 
                              name=data['name'], 
                              origin=data['origin'])

    def test_number_of_sources(self):
        sources = Source.objects.all()
        self.assertEqual(len(sources), 1)

    def test_data_of_sources(self):
        country = Country.objects.all()[0]
        data = {'url': 'www.test.com', 
                'name': 'TestNews', 
                'origin': country}
        source = Source.objects.all()[0]
        self.assertEqual(source.url, data['url'])
        self.assertEqual(source.name, data['name'])
        self.assertEqual(source.origin, data['origin'])


class ArticleTest(TestCase):

    def setUp(self):
        country = Country.objects.create(name="Argentina")
        data = {'url': 'www.test.com', 
                'name': 'TestNews', 
                'origin': country}
        source = Source.objects.create(url=data['url'], 
                                       name=data['name'], 
                                       origin=data['origin'])
        positive_text = """
        This is a positive text. What a great story. Excellent!
        I feel so much joy. This is fantastic! Awesome!
        I love Hungary!
        """
        negative_text = """
        This is a negative text. What a terrible story. Horrible!
        I feel so sad. This is depressing! Awful!
        I don't like China!
        """
        positive_data = {'url': 'www.test.com/positive_story',
                         'title': 'A Positive Story',
                         'text': positive_text,
                         'rating': 10,
                         'length': len(positive_text),
                         'source': source}
        negative_data = {'url': 'www.test.com/negative_story',
                         'title': 'A Negative Story',
                         'text': negative_text,
                         'rating': -10,
                         'length': len(negative_text),
                         'source': source}
        pos_article = Article.objects.create(url=positive_data['url'],
                                             title=positive_data['title'],
                                             text=positive_data['text'],
                                             rating=positive_data['rating'],
                                             length=positive_data['length'],
                                             source=positive_data['source'])
        neg_article = Article.objects.create(url=negative_data['url'],
                                             title=negative_data['title'],
                                             text=negative_data['text'],
                                             rating=negative_data['rating'],
                                             length=negative_data['length'],
                                             source=negative_data['source'])
        pos_article.get_countries()
        neg_article.get_countries()

    def test_number_of_articles(self):
        articles = Article.objects.all()
        self.assertEqual(len(articles), 2)

    def test_data_of_articles(self):
        articles = Article.objects.all()
        source = Source.objects.all()[0]
        positive_text = """
        This is a positive text. What a great story. Excellent!
        I feel so much joy. This is fantastic! Awesome!
        I love Hungary!
        """
        hungary = Country.objects.filter(name="Hungary")[0]
        china = Country.objects.filter(name="China")[0]
        pos_data = {'url': 'www.test.com/positive_story',
                    'title': 'A Positive Story',
                    'text': positive_text,
                    'rating': 10,
                    'length': len(positive_text),
                    'source': source}
        self.assertEqual(articles[0].url, pos_data['url'])
        self.assertEqual(articles[0].title, pos_data['title'])
        self.assertEqual(articles[0].text, pos_data['text'])
        self.assertEqual(articles[0].rating, pos_data['rating'])
        self.assertEqual(articles[0].length, pos_data['length'])
        self.assertEqual(articles[0].source, pos_data['source'])
        self.assertEqual(articles[0].countries.all()[0], hungary)
        

