from django.test import TestCase
from .models import Item


class TestModels(TestCase):
    # Tests if done if false by default

    def test_done_defaults_to_false(self):
        item = Item.objects.create(name="test to do item")
        self.assertFalse(item.done)


    def test_item_string_method_returns_name(self):
        item = Item.objects.create(name="test to do item")
        self.assertEqual(str(item), "test to do item")




