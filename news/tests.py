from django import test

class TestNews(test.TestCase):

    def test_news_index_page(self):
        client = test.Client()
        response = client.get('/news/')
        self.assertTemplateUsed(response, 'news/templates/index.html')