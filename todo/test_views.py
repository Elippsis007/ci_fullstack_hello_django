from django.test import TestCase
from .models import Item

# Create your tests here.

class TestViews(TestCase):
# To test HTTP response of the views we can use built-in HTTP client that comes with Django
# testing framework.
    def test_get_todo_list(self):
# '/' represents homepage.
        response = self.client.get('/')
        # Using assertEqual to confirm that the response.status code is equal to 200 (Successful HTTP respons, NOT 404)
        self.assertEqual(response.status_code, 200)
        # To confirm the correct template is in use (html) for the response.
        self.assertTemplateUsed(response, 'todo/todo_list.html')


    def test_get_add_item_page(self):
        response = self.client.get('/add')
        # Using assertEqual to confirm that the response.status code is equal to 200 (Successful HTTP respons, NOT 404)
        self.assertEqual(response.status_code, 200)
        # To confirm the correct template is in use (html) for the response.
        self.assertTemplateUsed(response, 'todo/add_item.html')


    def test_get_todo_list(self):
        item = Item.objects.create(name='Test Todo Item')
        response = self.client.get(f'/edit/{item.id}')
        # Using assertEqual to confirm that the response.status code is equal to 200 (Successful HTTP respons, NOT 404)
        self.assertEqual(response.status_code, 200)
        # To confirm the correct template is in use (html) for the response.
        self.assertTemplateUsed(response, 'todo/edit_item.html')

    def test_get_edit_item_page(self):
        item = Item.objects.create(name='Test Todo Item')
        response = self.client.get(f'/edit/{item.id}')
        self.assertTemplateUsed(response, 'todo/edit_item.html')


    def test_can_add_item(self):
        response = self.client.post('/add', {'name': 'Test Added Item'})
        self.assertRedirects(response, '/')
            

    def test_can_delete_item(self):
        item = Item.objects.create(name='Test Todo Item')
        response = self.client.get(f'/delete/{item.id}')
        # Using assertEqual to confirm that the response.status code is equal to 200 (Successful HTTP respons, NOT 404)
        self.assertRedirects(response, '/')
        # To confirm the correct template is in use (html) for the response.
        existing_items = Item.objects.filter(id=item.id)
        self.assertEqual(len(existing_items), 0)


    def test_can_toggle_item(self):
        item = Item.objects.create(name='Test Todo Item', done=True)
        response = self.client.get(f'/toggle/{item.id}')
        # Using assertEqual to confirm that the response.status code is equal to 200 (Successful HTTP respons, NOT 404)
        self.assertRedirects(response, '/')
        updated_item = Item.objects.get(id=item.id)
        self.assertFalse(updated_item.done)