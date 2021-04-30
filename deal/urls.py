from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt
#from .views import DealListView, SubscriptionsView

urlpatterns = [
    path('', views.index, name= 'index'),
    path('deals/', views.dashboad, name= 'dashboad'),
    path('deals/subscriptions/', views.manage_subscriptions, name = 'subscriptions'),
    path('add-deal/', views.add_deal, name = 'add-deal'),
    path('add-deal/address_assets/', views.address_asset, name = 'address_assets'),
    path('save/', views.save_deal, name = 'save_deal'),
    path('deal/<int:pk>', views.view_deal_detail, name ='deal-detail'),
    path('search-deals', csrf_exempt(views.search_deals),
         name="search_deals"),
    path('deal_delete/<int:pk>', views.deal_delete, name="deal_delete"),
  
  


]
