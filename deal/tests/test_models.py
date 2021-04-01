from django.test import TestCase, Client
from deal.models import Deals, ComputeDeals, Adress,AssetTypes
import json
from django.contrib.auth.models import User
from deal.config import *
import unittest
from unittest.mock import patch
import mock

import os

class TestModels(TestCase):

    def setUp(self):
        self.address1 = Adress.objects.create(city="New York City", state_code="NY")
        self.asset1 = AssetTypes.objects.create()
        self.compute1 = ComputeDeals.objects.create(period= 1, compare='below', percentage_compare_average_price=0)
        self.user = User.objects.create_user(username='testuser', email='test@company.com', password='12345')
        self.deal1 = Deals.objects.create(user=self.user, name='deal1', property_status='For Rent', adress=self.address1, assets=self.asset1, computeDeal=self.compute1)
        
        self.pk = self.deal1.pk
    
    def test_get_query_params(self):
        

        params = {'city': 'New York City', 'state_code': 'NY', 'postal_code': '', 'offset': '0', 'limit': 10, 'baths_min': None, 'beds_min': None, 'radius': None, 'price_min': None, 'sqft_min': None, 'age_min': None, 'lot_sqft_max': None, 'price_max': None, 'lot_sqft_min': None, 'prop_type': '', 'age_max': None, 'sort': '', 'sqft_max': None}
        self.assertEqual(self.deal1.get_query_params(), params )

  #  def test_search_query_GET(self):
   #     response = self.deal1.property_search_query(url_for_rent)
    #    self.assertEqual(response.status_code, 200)

        
   
    def test_property_search_query(self):
        fake_response = [{'meta': {'build': '3.23.144',}}]
        with patch("deal.models.Deals.property_search_query") as mock_response:
            mock_response.return_value.ok = True
            mock_response.return_value.json.return_value = fake_response
            self.assertEqual(self.deal1.property_search_query(url_for_rent).ok,True )
            self.assertEqual(self.deal1.property_search_query(url_for_rent).json(),fake_response)

            mock_response.return_value.ok = False
            
            self.assertEqual(self.deal1.property_search_query(url_for_rent).ok,False )
        

    




       