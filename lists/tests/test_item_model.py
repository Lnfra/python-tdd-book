from django.test import TestCase
from lists.models import Item


class TestItemModel(TestCase):

    def test_saving_and_retrieving_items(self):

        first_item = Item()
        first_item.text = 'first list item'
        first_item.save()

        second_item = Item()
        second_item.text = 'second list item'
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'first list item')
        self.assertEqual(second_saved_item.text, 'second list item')

