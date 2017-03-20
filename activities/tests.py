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

		self.assertEqual(Item.objects.count(), 1)
		new_item = Item.objects.first()
		self.assertEqual(new_item.text, 'A new activity item')

	def test_redirects_after_POST(self):
		response = self.client.post('/', data={'item_text': 'A new activity item'})
		
		self.assertEqual(response.status_code, 302)
		self.assertEqual(response['location'], '/')

	def test_only_saves_items_when_necessary(self):
		self.client.get('/')
		self.assertEqual(Item.objects.count(), 0)

class ItemModelTest(TestCase):

	def test_saving_and_retrieving_items(self):
		new_item = Item()
		new_item.text = 'The new item'
		new_item.save()

		saved_items = Item.objects.all()
		self.assertEqual(saved_items.count(), 1)

		only_item = saved_items[0]
		self.assertEqual(only_item.text, 'The new item')