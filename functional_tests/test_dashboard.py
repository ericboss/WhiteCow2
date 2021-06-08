from deal.views import dashboad
from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
import time
from django.test import TestCase, Client
from django.contrib.auth.models import User
from deal.models import *
from deal.view_method import *
import pandas as pd
class TestIndexPage(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome('functional_tests/chromedriver')
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', email='test@company.com', password='12345')

        self.browser.get(self.live_server_url)
        self.browser.find_element_by_id('signin').click()
        time.sleep(3)
        self.browser.find_element_by_id("username-signin").send_keys("testuser")
        self.browser.find_element_by_id("password-signin").send_keys("12345")
        self.browser.find_element_by_id("login-submit").click()

        self.deal_df = pd.read_csv('/Users/ericboss/Documents/GitHub/WhiteCow2/deal/deal_df.csv')
        self.deal = Deals.objects.create(owner = self.user, name="test_deal")
        Adress.objects.create(owner=self.user,deal=self.deal,city="New York City",state_code="NY")
        AssetsForSale.objects.create(owner=self.user,deal=self.deal)

        self.deal_df['owner'] = self.user
        self.deal_df['deal'] = self.deal
        self.deal_df.drop('Unnamed: 0',axis=1,inplace=True)
        self.deal_df.drop('Unnamed: 0.1',axis=1,inplace=True)

        entries = []       
    
        for e in self.deal_df.T.to_dict().values():

            entries.append(SubscriptionDataForSale(**e))
        
        SubscriptionDataForSale.objects.bulk_create(entries)

        self.setup=Setup.objects.create(owner= self.user,deal = self.deal,title="test_deal")
    def tearDown(self) :
        self.browser.close()

    def test_create_deal_redirect_link(self):

        self.browser.find_element_by_id("create-deal").click()

        createdeal_url = self.live_server_url +reverse('address_assets')

        self.assertEquals(self.browser.current_url,createdeal_url)

    
    def test_view_deal_redirect_link(self):

        self.browser.find_element_by_id("view-deal").click()

        viewdeal_url = self.live_server_url +reverse('view')

        self.assertEquals(self.browser.current_url,viewdeal_url)
    

    def test_email_subscription_redirect_link(self):

        self.browser.find_element_by_id("email-subscriptions").click()

        email_subscriptions_url = self.live_server_url +reverse('subscriptions')

        self.assertEquals(self.browser.current_url,email_subscriptions_url )
    

    def test_create_deal(self):
        
    

        self.browser.find_element_by_id("view-deal").click()

        viewdeal_url = self.live_server_url +reverse('deal-detail',args=[self.deal.pk])
        self.browser.find_element_by_id("view-deal"+str(self.deal.pk)).click()
        self.assertEquals(self.browser.current_url,viewdeal_url )


    def test_email_subscription_deal(self):
        
    

        self.browser.find_element_by_id("email-subscriptions").click()

        subscriptions_url = self.live_server_url +reverse('subscriptions')
       # self.browser.find_element_by_id("subscriptions").click()
        self.browser.find_element_by_id("edit_subscription"+str(self.setup.pk)).click()
        self.assertEquals(self.browser.current_url,subscriptions_url )
        self.assertEquals(self.browser.find_element_by_id("setup-name"+str(self.setup.pk)).text,"test_deal's deal" )