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

        self.address1 = Adress.objects.create(city="New York City", state_code="NY", postal_code="")
        self.asset1 = AssetsForSale.objects.create()
        
        self.user = User.objects.create_user(username='testuser', email='test@company.com', password='12345')
        self.deal1 = Deals.objects.create(owner=self.user, name='deal1', property_status='Sale')
        
        self.pk = self.deal1.pk

        self.deal_detail_url = reverse('deal-detail', args=[self.pk])
        self.delete_url = reverse('deal_delete', args = [self.pk])
     

    def test_index_GET(self):

        
        response = self.client.get(self.index_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'deal/Views/dashboard.html')

    def test_add_deal_url_GET(self):
        login = self.client.login(username='testuser', password='12345')

        response = self.client.get(self.add_deal_url)
        

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'deal/Views/add-deal.html')

    def test_display_GET(self):
        login = self.client.login(username='testuser', password='12345')

        response = self.client.get(self.display_url)
        


        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'deal/display.html')

    def test_deals_new_GET(self):
        login = self.client.login(username='testuser', password='12345')

        response = self.client.get(self.deals_new_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'deal/deal-form.html')

    def test_edit_GET(self):
        
        login = self.client.login(username='testuser', password='12345')
        response = self.client.get(self.edit_deal_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'deal/edit.html')

    
    def test_delete_GET(self):
        login = self.client.login(username='testuser', password='12345')

        response = self.client.get(self.delete_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'deal/delete.html')

    def test_display_specific_GET(self):
        login = self.client.login(username='testuser', password='12345')

        response = self.client.get(self.display_specific_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'deal/display_specific.html')
    
    def test_edit_POST(self):
        login = self.client.login(username='testuser', password='12345')

        deal = Deals.objects.get(pk = self.pk)
        deal_form = DealsForm( instance=deal)
        response = self.client.post(self.edit_deal_url, {'edit_form':deal_form, 'deal':deal})

        self.assertEquals(response.status_code, 200)
        self.assertEquals(self.deal1.name, 'deal1')

    def test_specific_deal_POST(self):
        login = self.client.login(username='testuser', password='12345')

        deal = Deals.objects.get(pk = self.pk)
        address = Adress.objects.get(pk = self.pk) 
        asset = AssetTypes.objects.get(pk = self.pk) 
        compute = ComputeDeals.objects.get(pk = self.pk)


        deal_form = DealsForm( instance=deal)
        form_adress = DealAddressForm(instance=address)
        form_compute = DealComputeDealForm(instance=compute)
        form_asset = DealAssetTypeForm(instance=asset)

        response = self.client.post(self.display_specific_url, {'deal':deal,'deal_form': deal_form,'adress':form_adress, 'compute':form_compute, 'asset':form_asset})

        self.assertEquals(response.status_code, 200)
        self.assertEquals(self.deal1.name, 'deal1')


    def test_create_deal_POST(self):
        login = self.client.login(username='testuser', password='12345')

        deal = Deals.objects.get(pk = self.pk)
        address = Adress.objects.get(pk = self.pk) 
        asset = AssetTypes.objects.get(pk = self.pk) 
        compute = ComputeDeals.objects.get(pk = self.pk)


        deal_form = DealsForm(data={'name':'deal2', 'property_status':'For Rent'})
        form_adress = DealAddressForm(instance=address)
        form_compute = DealComputeDealForm(instance=compute)
        form_asset = DealAssetTypeForm(instance=asset)

        response = self.client.post(self.deals_new_url, {'deal':deal,'deal_form': deal_form,'adress':form_adress, 'compute':form_compute, 'asset':form_asset})
        
        self.assertEquals(response.status_code, 200)
       
       
      
    
    def test_delete_POST(self):
        login = self.client.login(username='testuser', password='12345')

        deal = Deals.objects.get(pk = self.pk)
        
        response = self.client.post(self.delete_url, {'deal':deal})

        self.assertEquals(response.status_code, 302)
        