from django.contrib import admin
from .models import (Deals, PropertyStatus, Adress,AssetsForRent,Sort,PropertyType,ExpandSearchRadius,
HomeSize, InUnitFeatures,CommunityAmmenities,Ok,SortSale, PropertyTypeSale, PropertyTypeNycOnly, NoHoaFee,
HomeSizeMinSale, HomeSizeMaxSale,LotSize,Stories,Garage,HeatingCooling,InsideRooms,OutsideFeatures,LotViews,CommunityAmmenitiesSale,
FeaturesInNycOnly)

admin.site.register(PropertyStatus)
admin.site.register(Deals)
admin.site.register(Adress)
admin.site.register(AssetsForRent)
admin.site.register(Sort)
admin.site.register(PropertyType)
admin.site.register(ExpandSearchRadius)
admin.site.register(HomeSize)
admin.site.register(InUnitFeatures)
admin.site.register(CommunityAmmenities)
admin.site.register(Ok)

admin.site.register(SortSale)
admin.site.register(PropertyTypeSale)
admin.site.register(PropertyTypeNycOnly)
admin.site.register(NoHoaFee)
admin.site.register(HomeSizeMinSale)
admin.site.register(HomeSizeMaxSale)
admin.site.register(LotSize)
admin.site.register(Stories)
admin.site.register(Garage)
admin.site.register(HeatingCooling)
admin.site.register(InsideRooms)
admin.site.register(OutsideFeatures)
admin.site.register(LotViews)
admin.site.register(CommunityAmmenitiesSale)
admin.site.register(FeaturesInNycOnly)