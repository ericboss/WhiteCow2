from django.test import TestCase, Client
from django.urls import reverse
from deal.models import Deals, Adress,AssetsForSale
import json
from django.contrib.auth.models import User


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.index_url = reverse('index')
        self.add_deal_url = reverse('add-deal')
        self.address_assets_url = reverse('address_assets')
        self.save_deal_url = reverse('save_deal')

       # self.address1 = Adress.objects.create(city="New York City", state_code="NY", postal_code="")
       # self.asset1 = AssetsForSale.objects.create()
        
       # self.user = User.objects.create_user(username='testuser', email='test@company.com', password='12345')
       # self.deal1 = Deals.objects.create(owner=self.user, name='deal1', property_status='Sale')
        
       # self.pk = self.deal1.pk

       # self.deal_detail_url = reverse('deal-detail', args=[self.pk])
        #self.delete_url = reverse('deal_delete', args = [self.pk])
     

    def test_index_GET(self):

        
        response = self.client.get(self.index_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'deal/Views/dashboard.html')

    
    