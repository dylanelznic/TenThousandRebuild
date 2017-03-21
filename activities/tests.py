from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string

from activities.views import home_page
from activities.models import Activity

# Create your tests here.

class HomePageTest(TestCase):

	def test_root_url_resolves_to_home_page_view(self):
		found = resolve('/')
		self.assertEqual(found.func, home_page)

	def test_uses_home_template(self):
		response = self.client.get('/')
		self.assertTemplateUsed(response, 'home.html')

	def test_can_save_a_POST_request(self):
		response = self.client.post('/', data={'activity_text': 'A new activity'})

		self.assertEqual(Activity.objects.count(), 1)
		new_activity = Activity.objects.first()
		self.assertEqual(new_activity.text, 'A new activity')

	def test_redirects_after_POST(self):
		response = self.client.post('/', data={'activity_text': 'A new activity'})
		
		self.assertEqual(response.status_code, 302)
		self.assertEqual(response['location'], '/activities/the-only-activity-in-the-world/')

	def test_only_saves_activity_when_necessary(self):
		self.client.get('/')
		self.assertEqual(Activity.objects.count(), 0)

class ActivityModelTest(TestCase):

	def test_saving_and_retrieving_activity(self):
		new_activity = Activity()
		new_activity.text = 'The new activity'
		new_activity.save()

		saved_activity = Activity.objects.all()
		self.assertEqual(saved_activity.count(), 1)

		only_activity = saved_activity[0]
		self.assertEqual(only_activity.text, 'The new activity')

class LiveViewTest(TestCase):

	def test_displays_activity(self):
		Activity.objects.create(text='Dancing')

		response = self.client.get('/activities/the-only-activity-in-the-world/')

		self.assertContains(response, 'Dancing')

		## BOOKMARK: Chapter 6
		## Taking a first, self-contained step: one new URL

	def test_uses_activity_template(self):
		response = self.client.get('/activities/the-only-activity-in-the-world/')
		self.assertTemplateUsed(response, 'activity.html')