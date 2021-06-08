from deal.views import dashboad
from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
import time
from django.test import TestCase, Client
from django.contrib.auth.models import User


class TestIndexPage(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome('functional_tests/chromedriver')
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', email='test@company.com', password='12345')

        self.client.login(username='testuser', password='12345')
        

    def tearDown(self) :
        self.browser.close()

    def test_index_page(self):
        self.browser.get(self.live_server_url)

        welcome = self.browser.find_element_by_name('welcome')

        self.assertEqual(welcome.text, "Welcome to the WhiteCow Project")
        #time.sleep(10)


    def test_display_signin_form(self):
        
        main_url = self.live_server_url +'/'
        self.browser.get(self.live_server_url)
        self.browser.find_element_by_id('signin').click()
        time.sleep(3)
        self.assertEqual(self.browser.current_url, main_url)

        
    def test_display_signup_form(self):
        
        main_url = self.live_server_url +'/'
        self.browser.get(self.live_server_url)
        self.browser.find_element_by_id('signup').click()
        time.sleep(3)
        self.assertEqual(self.browser.current_url, main_url)

    def test_login_redirect_dashboard(self):

        main_url = self.live_server_url +reverse('dashboad')
        self.browser.get(self.live_server_url)
        self.browser.find_element_by_id('signin').click()
        time.sleep(3)
        self.browser.find_element_by_id("username-signin").send_keys("testuser")
        self.browser.find_element_by_id("password-signin").send_keys("12345")
        self.browser.find_element_by_id("login-submit").click()

        self.assertEqual(self.browser.current_url, main_url)
    
   


