from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string

from activities.views import home_page
from activities.models import Item

# Create your tests here.

class HomePageTest(TestCase):

	def test_root_url_resolves_to_home_page_view(self):
		found = resolve('/')
		self.assertEqual(found.func, home_page)

	def test_uses_home_template(self):
		response = self.client.get('/')
		self.assertTemplateUsed(response, 'home.html')

	def test_can_save_a_POST_request(self):
		response = self.client.post('/', data={'item_text': 'A new activity item'})
		self.assertIn('A new activity item', response.content.decode())
		self.assertTemplateUsed(response, 'home.html')

class ItemModelTest(TestCase):

	def test_saving_and_retrieving_items(self):
		new_item = Item()
		new_item.text = 'The new item'
		new_item.save()

		saved_item = Item.objects.all()
		self.assertEqual(saved_item.count(), 1)

		self.assertEqual(saved_item.text, 'The new item')