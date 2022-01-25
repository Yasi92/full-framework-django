from django.test import TestCase
from .forms import ItemForm


class TestItemForm(TestCase):

    def test_item_name_is_required(self):
        # if the name is empty
        form = ItemForm({'name' : ''})
        # raise invalid form
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required.')


    def test_done_field_is_not_required(self):
        # if the name is filled eventhought the done is not validate the form
        form = ItemForm({'name' : 'Test todo item'})
        self.assertTrue(form.is_valid())


    def test_fields_are_explicit_in_form_metaclass(self):
        form = ItemForm()
        # only display the name and done fields
        self.assertEqual(form.Meta.fields, ['name', 'done'])

