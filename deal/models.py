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

# Create your models here.
class Deals(models.Model):
    name = models.CharField(max_length=30)
    property_status = models.CharField(max_length=10)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Deals'

class PropertyStatus(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
    

    class Meta:
        verbose_name_plural = 'PropertyStatus'

class Adress(models.Model):
    """
    Addres Class contains attributes necessary for saving the Adress of a deal.
    """
    deal = models.OneToOneField(Deals, on_delete=models.CASCADE, related_name="deal_address", blank=True, null=True)
    city = models.CharField(max_length=40)
    state_code = models.CharField(max_length=10)
    location = models.CharField(max_length=10, blank=True, default='') #postal code

    offset = models.CharField(max_length=10, default="0")
    limit = models.IntegerField(default=30)

    def __str__(self):
        return "{}, {}".format(self.city, self.state_code)

class AssetsForRent(models.Model):

    deal = models.OneToOneField(Deals, on_delete=models.CASCADE, related_name="deal_assets_for_rent", blank=True, null=True)
    
    sort = models.CharField(max_length=255, blank=True, null=True)
    price_min = models.IntegerField(blank=True, null=True)
    price_max = models.IntegerField(blank=True, null=True)
    beds_min = models.IntegerField(blank=True, null=True)
    beds_max = models.IntegerField(blank=True, null=True)
    baths_min = models.IntegerField(blank=True, null=True)
    baths_max = models.IntegerField(blank=True, null=True)
    property_type = models.CharField(max_length=255, blank=True, null=True)
    expand_search_radius = models.CharField(max_length=25, blank=True, null=True)
    include_nearby_areas_slug_id = models.CharField(max_length=255, blank=True, null=True)
    home_size_min = models.IntegerField(blank=True, null=True)
    home_size_max = models.IntegerField(blank=True, null=True)
    in_unit_features = models.CharField(max_length=255, blank=True, null=True)
    community_ammenities = models.CharField(max_length=255, blank=True, null=True)
    cats_ok = models.BooleanField(null=True, blank=True)
    dogs_ok = models.BooleanField(null=True, blank=True)


    def __str__(self):
        return "Assets for rent"

class AssetsForSale(models.Model):
    
    deal = models.OneToOneField(Deals, on_delete=models.CASCADE, related_name="deal_assets_for_sale", blank=True, null=True)

    sort = models.CharField(max_length=255, blank=True, null=True)
    price_min = models.IntegerField(blank=True, null=True)
    price_max = models.IntegerField(blank=True, null=True)
    beds_min = models.IntegerField(blank=True, null=True)
    beds_max = models.IntegerField(blank=True, null=True)
    baths_min = models.IntegerField(blank=True, null=True)
    baths_max = models.IntegerField(blank=True, null=True)
    property_type = models.CharField(max_length=255, blank=True, null=True)
    property_type_nyc_only = models.CharField(max_length=255, blank=True, null=True)
    new_construction = models.CharField(max_length=25, blank=True, null=True)
    hide_pending_contingent = models.CharField(max_length=25, blank=True, null=True)
    has_virtual_tours = models.CharField(max_length=25, blank=True, null=True)
    has_3d_tours = models.CharField(max_length=25, blank=True, null=True)
    hide_foreclosure = models.CharField(max_length=25, blank=True, null=True)
    price_reduced = models.CharField(max_length=25, blank=True, null=True)
    open_house = models.CharField(max_length=25, blank=True, null=True)
    keywords = models.CharField(max_length=255, blank=True, null=True)
    no_hoa_fee = models.CharField(max_length=25, blank=True, null=True)
    hoa_max = models.IntegerField(blank=True, null=True)
    days_on_realtor = models.CharField(max_length=25, blank=True, null=True)
    expand_search_radius = models.CharField(max_length=25, blank=True, null=True)
    include_nearby_areas_slug_id = models.CharField(max_length=255, blank=True, null=True)
    home_size_min = models.IntegerField(blank=True, null=True)
    home_size_max = models.IntegerField(blank=True, null=True)
    lot_size_min = models.IntegerField(blank=True, null=True)
    lot_size_max = models.IntegerField(blank=True, null=True)
    stories = models.CharField(max_length=25, blank=True, null=True)
    garage = models.CharField(max_length=25, blank=True, null=True)
    heating_cooling = models.CharField(max_length=25, blank=True, null=True)
    inside_rooms = models.CharField(max_length=255, blank=True, null=True)
    outside_features = models.CharField(max_length=255, blank=True, null=True)
    lot_views = models.CharField(max_length=255, blank=True, null=True)
    community_ammenities = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return "Assets for sale"

class ComputeDeals(models.Model):
    """
    Compute Deals Class contains attributes for making some computations for the deal.
    - period: The user might want to compare data against average market price for the last x period( 1 month, 3 months etc)
    - compare: The user might want to get data that are above/below average market price
    - percentage_compare_average_price: The user might want to get data that are X% above/below average market price.
    """
    
    deal = models.OneToOneField(Deals, on_delete=models.CASCADE, related_name="deal_compute_deal", blank=True, null=True)
    period = models.IntegerField( null=True, blank=True)
    compare = models.CharField(max_length=20, default=None)
    percentage_compare_average_price = models.IntegerField(default=0)



class SubscriptionDataForRent(models.Model):

    deal = models.OneToOneField(Deals, on_delete=models.CASCADE, related_name="deal_subscription_for_rent", blank=True, null=True)
    photos = models.JSONField(blank=True, null = True)
    branding = models.JSONField(blank=True, null = True)
    other_listings = models.JSONField(blank=True, null = True)
    list_price_min = models.IntegerField(blank=True, null = True)
    href = models.CharField(max_length=255,blank=True, null = True )
    when_indexed = models.DateTimeField(blank=True, null = True )
    last_sold_price = models.FloatField(blank=True, null = True )
    property_id = models.CharField(max_length=255,blank=True, null = True )
    advertisers = models.JSONField(blank=True, null = True)
    virtual_tours = models.CharField(max_length=50,blank=True, null = True )
    seller_promotion = models.CharField(max_length=50,blank=True, null = True )
    listing_id = models.CharField(max_length=50,blank=True, null = True )
    price_reduced_amount = models.CharField(max_length=50,blank=True, null = True )
    location = models.JSONField(blank=True, null = True)
    last_update_date = models.DateTimeField(blank=True, null = True )
    source = models.JSONField(blank=True, null = True)
    permalink = models.CharField(max_length=255,blank=True, null = True )
    list_date = models.DateTimeField(blank=True, null = True )
    open_houses = models.CharField(max_length=50,blank=True, null = True )
    last_sold_date = models.DateField(blank=True, null = True )
    last_price_change_date = models.DateField(blank=True, null = True )
    description = models.JSONField(blank=True, null = True)
    last_price_change_amount = models.CharField(max_length=50,blank=True, null = True )
    price_reduced_date = models.DateField(blank=True, null = True )
    property_history = models.CharField(max_length=50,blank=True, null = True )
    photo_count = models.IntegerField(blank=True, null = True)
    list_price = models.CharField(max_length=50,blank=True, null = True )
    lead_attributes = models.JSONField(blank=True, null = True)
    list_price_max = models.IntegerField(blank=True, null = True)
    tags = models.CharField(max_length=255,blank=True, null = True )
    pet_policy = models.JSONField(blank=True, null = True)
    products = models.JSONField(blank=True, null = True)
    suppression_flags = models.CharField(max_length=50,blank=True, null = True )
    status = models.CharField(max_length=10,blank=True, null = True )
    flags = models.JSONField(blank=True, null = True)
    community = models.CharField(max_length=50,blank=True, null = True )
    matterport = models.BooleanField(blank=True, null = True )
    primary_photo = models.JSONField(blank=True, null = True)


class SubscriptionDataForSale(models.Model):

    deal = models.OneToOneField(Deals, on_delete=models.CASCADE, related_name="deal_subscription_for_sale", blank=True, null=True)
    primary_photo = models.JSONField(blank=True, null = True)
    last_update_date = models.DateTimeField(blank=True, null = True )
    source = models.JSONField(blank=True, null = True)
    tags = models.CharField(max_length=255,blank=True, null = True )
    permalink = models.CharField(max_length=255,blank=True, null = True )
    status = models.CharField(max_length=10,blank=True, null = True )
    list_date = models.DateTimeField(blank=True, null = True )
    open_houses = models.CharField(max_length=50,blank=True, null = True )
    description = models.JSONField(blank=True, null = True)
    branding = models.JSONField(blank=True, null = True)
    list_price = models.IntegerField(blank=True, null = True)
    lead_attributes = models.JSONField(blank=True, null = True)
    property_id = models.CharField(max_length=255,blank=True, null = True )
    photos = models.JSONField(blank=True, null = True)
    flags = models.JSONField(blank=True, null = True)
    community = models.CharField(max_length=50,blank=True, null = True )
    products = models.JSONField(blank=True, null = True)
    virtual_tours = models.CharField(max_length=50,blank=True, null = True )
    other_listings = models.JSONField(blank=True, null = True)
    listing_id = models.CharField(max_length=50,blank=True, null = True )
    price_reduced_amount = models.CharField(max_length=50,blank=True, null = True )
    location = models.JSONField(blank=True, null = True)
    matterport = models.BooleanField(blank=True, null = True )

    


    

    
    



class Item(models.Model):
    video = EmbedVideoField()  # same like models.URLField()
