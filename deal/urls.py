from django.urls import path
from . import views
#from .views import DealListView, SubscriptionsView

urlpatterns = [
    path('', views.index, name= 'index'),
    path('deals/subscriptions/', views.manage_subscriptions, name = 'subscriptions'),
    path('deals/display/', views.display_search_query, name = 'display'),
     path('deals/save/', views.saveDeal, name = 'save'),
    path('deals/new/', views.make_query, name = 'deals-new'),
    path('deals/edit/<int:pk>/', views.edit, name = 'edit'),
    path('deals/view/<int:pk>/', views.view_deal, name = 'view_deal'),
    path('deals/view/specific/<int:pk>/', views.detail_view_deal, name = 'detail_view_deal'),
    path('deals/refresh/<int:pk>/', views.refresh_deal, name = 'refresh'),
    path('deals/detail_refresh/<int:pk>/', views.detail_view_refresh, name = 'detail_view_refresh'),
    path('deals/save_refresh/<int:pk>/', views.save_refresh, name = 'save_refresh'),
    path('deals/delete/<int:pk>/', views.delete, name = 'delete'),
     path('deals/detail/<int:pk>/', views.detail, name = 'display_detail'),
    path('deals/deal/<int:pk>/', views.deal_diaplay_specific_search_id, name = 'display_specific'),
  
    path('',views.videos)

]