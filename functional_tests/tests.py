from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(LiveServerTestCase):

	def setUp(self):
		self.browser = webdriver.Chrome()

	def tearDown(self):
		self.browser.quit()

	def test_can_create_an_activity_and_retrieve_it_later(self):

		# User has been wanting to keep track of how long they have been programming. 
		# User finds tenthousand and checks out its homepage
		self.browser.get(self.live_server_url)

		# User notices the page title and header mention progress tracker functionality
		self.assertIn('Ten Thousand', self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('Progress Tracker', header_text)

		# User is invited to sign up for an account
		pass

		# After signing up for an account, the user is immediately prompted to begin 
		# tracking a new activity
		inputbox = self.browser.find_element_by_id('id_new_activity')

		self.assertEqual(inputbox.get_attribute('placeholder'),
			'Enter a new activity'
		)

		# User types "Programming" into a text box
		inputbox.send_keys('Programming')

		# When the user hits enter, the page updates, and now the page has 
		# a header, "Programming"
		inputbox.send_keys(Keys.ENTER)
		time.sleep(1)

		activity_header_text = self.browser.find_element_by_tag_name('header').text
		self.assertIn('Programming', activity_header_text,
			f"New activity did not appear in <header>. Contents were:\n{activity_header_text}"
		)

		# There is a large timer beneath the header, with 'start' and 'stop'
		# buttons bellow it

		self.fail('Finish writing the functional test!')

		# The User hits start and sees the timer running

		# The User hits stop and sees the timer stop at the current time

		# Curious, the User closes the tab and reopens it to check if the website
		# has saved their time
		# Upon returning, the User is still signed on and finds the same time
		# still on the timer

		# Satisfied, the User starts the timer again and returns to programming