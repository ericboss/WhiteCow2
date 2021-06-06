from django.test import SimpleTestCase
from django.urls import reverse, resolve
from deal.views import index,view_deal,dashboad,add_deal,address_asset, save_deal
import xmlrunner, unittest

class TestUrls(SimpleTestCase):


    def test_index_is_resolved(self):
        url = reverse('index')
        self.assertEqual(resolve(url).func, index)

    def test_add_deal(self):
        url = reverse('add-deal')
        self.assertEqual(resolve(url).func, add_deal)
    
    def test_address_assets(self):
        url = reverse('address_assets')
        self.assertEqual(resolve(url).func, address_asset)
    
    def test_save_deal(self):
        url = reverse('save_deal')
        self.assertEqual(resolve(url).func, save_deal)
    
  
    
if __name__ == '__main__':

    unittest.main(testRunner=xmlrunner.XMLTestRunner(),failfast=False,buffer=False,catchbreak=False)
 

    
    