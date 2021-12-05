from django.test import TestCase
from .forms import ItemForm

# Class will inherit TestCase and contain all the tests for this form.
class TestItemForm(TestCase):
    
    # This test is making sure the name field is required in order for a user to create an item.
    def test_item_name_is_required(self):
        # Creating a form and in this case creating it without a name.
        # So that it simulates a user who submits a form with out completing the form.
        form = ItemForm({'name': ''})
        # The form is not valid, so using "assertFalse" will make sure it's not valid.
        self.assertFalse(form.is_valid())
        # When a form is invalid, it should send back a dictionary of fields where there were
        # errors and error messages.
        self.assertIn('name', form.errors.keys())
        # This checks if the error message on the name field is for "This field is required."
        # The [0] verifies that the first item in that list is our string matching the "This field is required."
        self.assertEqual(form.errors['name'][0], 'This field is required.')
    

    # This test is making sure that the "done" field is not required.
    def test_done_field_is_not_required(self):
        # Creating a form and sending only a name.
        form = ItemForm({'name': 'Test Todo Item'})
        # Testing the form is valid as it should be without selecting a done status.
        self.assertTrue(form.is_valid())

    def test_fields_are_explicit_in_form_metaclass(self):
        form = ItemForm()
        self.assertEqual(form.Meta.fields, ['name', 'done'])
        