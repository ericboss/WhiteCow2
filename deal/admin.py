from django.contrib import admin
from .models import Deals, Adress,AssetTypes,ComputeDeals

# Register your models here.
admin.site.register(Adress)
admin.site.register(Deals)
admin.site.register(AssetTypes)
admin.site.register(ComputeDeals)


from django.contrib import admin
from embed_video.admin import AdminVideoMixin
from .models import Item

class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

admin.site.register(Item, MyModelAdmin)