from django.test import TestCase

from lists.models import Item


class TestHomePage(TestCase):
    def test_home_page_returns_correct_html(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_can_save_a_post_request(self):
        self.client.post('/', data={'item_text': 'A new list item'})

        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new list item')

    def test_redirects_after_a_post_request(self):
        response = self.client.post('/', data={'item_text': 'A new item list'})

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/')

    def test_only_saves_item_when_necessary(self):
        self.client.get('/')
        self.assertEqual(Item.objects.count(), 0)

    def test_displays_all_list_items(self):
        Item.objects.create(text='Item1')
        Item.objects.create(text='Item2')

        response = self.client.get('/')

        self.assertIn('Item1', response.content.decode())
        self.assertIn('Item2', response.content.decode())
