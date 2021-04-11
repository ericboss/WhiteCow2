from django.urls import path
from . import views
#from .views import DealListView, SubscriptionsView

urlpatterns = [
    path('', views.index, name= 'index'),
    path('add-deal', views.add_deal, name = 'add-deal'),
    path('add-deal/address_assets', views.address_asset, name = 'address_assets'),
  
  


]
