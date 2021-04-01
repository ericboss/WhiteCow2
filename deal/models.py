from embed_video.fields import EmbedVideoField
from django.db import models
import pandas as pd
import numpy as np
import requests
from .config import *
import json
from django.contrib.auth.models import User
import logging

logger = logging.getLogger('django')


class Adress(models.Model):
    """
    Addres Class contains attributes necessary for saving the Adress of a deal.
    """
    city = models.CharField(max_length=40)
    state_code = models.CharField(max_length=10)
    postal_code = models.CharField(max_length=10, blank=True, default='')

    def __str__(self):
        return "{}, {}".format(self.city, self.state_code)


class AssetTypes(models.Model):
    """
    AssetTypes Class contains attributes for the assets of a real esate property.Deal Class will use
     these assets along side with Adress,Computedeals class in order to comeout with  a deal.
    """

    PROP_TYPE_CHOICES = [('single_family', 'single_family'), ('multi_family', 'multi_family'),
                         ('condo', 'condo'), ('mobile', 'mobile'),
                         ('land', 'land'), ('farm', 'farm'), ('other', 'other')]
    SORT_CHOICES = [('sold_date', 'sold_date'), ('beds_high', 'beds_high'),
                    ('price_low', 'price_low'), ('price_high', 'price_high'), ('lot_sqft_high', 'lot_sqft_high')]

    offset = models.CharField(max_length=10, default="0")
    limit = models.IntegerField(default=10)
    baths_min = models.IntegerField(blank=True, null=True)
    beds_min = models.IntegerField(blank=True, null=True)
    radius = models.IntegerField(blank=True, null=True)
    price_min = models.IntegerField(blank=True, null=True)

    sqft_min = models.IntegerField(blank=True, null=True)
    age_min = models.IntegerField(blank=True, null=True)
    lot_sqft_max = models.IntegerField(blank=True, null=True)
    price_max = models.IntegerField(blank=True, null=True)
    lot_sqft_min = models.IntegerField(blank=True, null=True)
    prop_type = models.CharField(
        max_length=20, choices=PROP_TYPE_CHOICES, blank=True, default='')
    age_max = models.IntegerField(blank=True, null=True)
    sort = models.CharField(
        max_length=20, choices=SORT_CHOICES, blank=True, default='')
    sqft_max = models.IntegerField(blank=True, null=True)


class ComputeDeals(models.Model):
    """
    Compute Deals Class contains attributes for making some computations for the deal.
    - period: The user might want to compare data against average market price for the last x period( 1 month, 3 months etc)
    - compare: The user might want to get data that are above/below average market price
    - percentage_compare_average_price: The user might want to get data that are X% above/below average market price.
    """
    PERIOD_CHOICES = [(1, '1 month'), (3, '3 months'),
                      (6, '6 months'), (12, 'One year')]
    COMPARE_CHOICES = [('below', 'below'),
                       ('above', 'above'), ('equals', 'equals')]

    period = models.IntegerField(
        choices=PERIOD_CHOICES, null=True, blank=True)
    compare = models.CharField(
        max_length=20, choices=COMPARE_CHOICES, default=None)
    percentage_compare_average_price = models.IntegerField(default=0)

    def get_percentage_compare_average_price(self):
        return self.percentage_compare_average_price


class Deals(models.Model):
    """
    Deals class is for coming up with real estate deals. As atttributes, it contains a foreignkey to adress, ComputeDeals and 
    AssetTypes class. Aded to that the deal has a name,
    - property_status: whether the property if for rent or for sale
    - user: We want to compute and store deals per user
    - ReceiveEmail: option for whether the user  wants to receive email notifications
    - days: The user has a soption to receive emails daily or during weekends
    - time: The user can have as option to choose at what time he/she will like to receive notifications 
    """
    PROPERTY_STATUS_CHOICES = [('For Rent', 'For Rent'), ('For Sale', 'For Sale')
                               ]
    DAY_CHOICES = [('mon,tue,wed,thu,fri,sat,sun', 'Daily'),
                   ('sat,sun', 'Weekends')]
    TIME_CHOICES = [(5, '5:00am'), (6, '6:00am'), (7, '7:00am'),
                    (8, '8:00am'), (17, '5:00pm'), (21, '9:00pm'), (22, '10:00pm')]

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="Deals", null=True)
    name = models.CharField(max_length=20)
    property_status = models.CharField(
        max_length=20, choices=PROPERTY_STATUS_CHOICES, default='For Rent')
    adress = models.ForeignKey('Adress', on_delete=models.CASCADE)
    assets = models.ForeignKey('AssetTypes', on_delete=models.CASCADE)
    computeDeal = models.ForeignKey('ComputeDeals', on_delete=models.CASCADE)
    ReceveEmail = models.BooleanField(default=True)
    days = models.CharField(
        max_length=100, choices=DAY_CHOICES,  default='Daily')
    time = models.IntegerField(choices=TIME_CHOICES,
                               null=True, blank=True)

    def __str__(self):
        return self.name
    
class SubscriptionData(models.Model):
    deal= models.ForeignKey('Deals', on_delete=models.CASCADE, blank=True, null = True)
    property_id= models.CharField(max_length=1000, blank=True, null = True)
    listing_id= models.IntegerField(blank=True, null=True)
    beds = models.IntegerField(blank=True, null=True)
    client_display_flags= models.JSONField(blank=True, null = True)
    products= models.CharField(max_length=1000, blank=True, null = True)
    agents= models.CharField(max_length=1000, blank=True, null = True)
    lead_forms= models.JSONField(blank=True, null = True)
    building_size = models.JSONField(blank=True, null = True)
    rdc_app_url= models.CharField(max_length=1000, blank=True, null = True)
    data_source_name= models.CharField(max_length=1000, blank=True, null = True)
    source= models.CharField(max_length=1000, blank=True, null = True)
    page_no= models.IntegerField(blank=True, null=True)
    rank= models.IntegerField(blank=True, null=True)
    list_tracking= models.CharField(max_length=1000, blank=True, null = True)
    photo_count = models.IntegerField(blank=True, null=True)
    prop_type = models.CharField(max_length=20, blank=True, null = True)
    list_date = models.CharField(max_length=20, blank=True, null = True)
    last_update = models.CharField(max_length=20, blank=True, null = True)
    year_built = models.FloatField(blank=True, null=True)
    listing_status = models.CharField(max_length=20, blank=True, null = True)
    prop_status = models.CharField(max_length=25, blank=True, null = True)
    address= models.JSONField(blank=True, null = True)
    lot_size = models.JSONField(blank=True, null = True)
    rdc_web_url = models.CharField(max_length=1000, blank=True, null = True)
    community = models.JSONField(blank=True, null = True)
    photos = models.JSONField(blank=True, null = True)


class SubscriptionDataForSale(models.Model):
    deal= models.ForeignKey('Deals', on_delete=models.SET_NULL, blank=True, null = True)
    property_id = models.CharField(max_length=1000, blank=True, null = True)
    listing_id = models.IntegerField(blank=True, null=True)
    products= models.CharField(max_length=1000, blank=True, null = True)
    rdc_web_url= models.CharField(max_length=1000, blank=True, null = True)
    prop_type= models.CharField(max_length=20, blank=True, null = True)
    address= models.JSONField(blank=True, null = True)
    branding= models.JSONField(blank=True, null = True)
    prop_status= models.CharField(max_length=25, blank=True, null = True)
    price= models.IntegerField(blank=True, null=True)
    baths_full= models.IntegerField(blank=True, null=True)
    baths= models.IntegerField(blank=True, null=True)
    beds= models.IntegerField(blank=True, null=True)
    building_size= models.JSONField(blank=True, null = True)
    agents= models.JSONField(blank=True, null = True)
    office= models.JSONField(blank=True, null = True)
    last_update= models.CharField(max_length=1000, blank=True, null = True)
    client_display_flags= models.JSONField(blank=True, null = True)
    lead_forms = models.JSONField(blank=True, null = True)
    photo_count= models.IntegerField(blank=True, null=True)
    thumbnail = models.CharField(max_length=1000, blank=True, null = True)
    page_no = models.IntegerField(blank=True, null=True)
    rank = models.IntegerField(blank=True, null=True)
    list_tracking= models.CharField(max_length=1000, blank=True, null = True)
    lot_size = models.JSONField(blank=True, null = True)
    mls = models.JSONField(blank=True, null = True)
    data_source_name = models.CharField(max_length=100, blank=True, null = True)
    baths_half  = models.FloatField(blank=True, null=True)
    virtual_tour = models.CharField(max_length=1000, blank=True, null = True)
    prop_sub_type = models.CharField(max_length=1000, blank=True, null = True)
    open_houses = models.CharField(max_length=1000, blank=True, null = True)


        


    

    


    

    
    



class Item(models.Model):
    video = EmbedVideoField()  # same like models.URLField()
