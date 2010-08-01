from django import test

class MicroblogViewTests(test.TestCase):
    fixtures = ('test_data', )

    def setUp(self):
        self.client = test.Client()

    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(200, response.status_code)
        self.assertTemplateUsed(response, 'microblog/templates/index.html')

    def test_edit(self):
        response = self.client.get('/edit/1')
        self.assertEqual(200, response.status_code)
        self.assertTemplateUsed(response, 'microblog/templates/edit.html')
        self.assertEqual(response.context['blog'].id, 1)

    def test_save_edit(self):
        response = self.client.post('/save_edit/1', {'user':1, 'message':'xxxxx'}, follow=True)
        self.assertEqual(response.redirect_chain, [('http://testserver/', 302)])

    def test_invalid_save_edit(self):
        response = self.client.post('/save_edit/1', {})
        self.assertTemplateUsed(response, 'microblog/templates/edit.html')
        self.assertTrue(response.context['blog_form'].errors)