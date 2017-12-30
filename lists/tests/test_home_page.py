from django.test import TestCase


class TestHomePage(TestCase):
    def test_home_page_returns_correct_html(self):
        response = self.client.post('/', data={'item_text': 'A new item list'})
        self.assertIn('A new item list', response.content.decode())
        self.assertTemplateUsed(response, 'home.html')
