from django.shortcuts import render,redirect
from .models import(Deals, PropertyStatus, Adress,AssetsForRent,Sort,PropertyType,ExpandSearchRadius,
HomeSize, InUnitFeatures,CommunityAmmenities,Ok,SortSale, PropertyTypeSale, PropertyTypeNycOnly, NoHoaFee,
HomeSizeMinSale, HomeSizeMaxSale,LotSize,Stories,Garage,HeatingCooling,InsideRooms,OutsideFeatures,LotViews,CommunityAmmenitiesSale,
FeaturesInNycOnly,AssetsForSale,SubscriptionDataForSale)
from django.contrib import messages
from .view_method import *
import json,requests
from datetime import datetime
from django_pandas.io import read_frame
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
import sys,six

# Create your views here.
def index(request):
    """
    This view is to display the landing page

    """

    return render(request, 'deal/Views/index.html')

# Create your views here.
def dashboad(request):
    """
    This view is to display the landing page

    """

    deal = Deals.objects.filter(owner =request.user)
    context = {'saved_deals':deal}
    return render(request, 'deal/Views/dashboard.html',context)

deal_data =None
def add_deal(request):
    """
    Form for deal name and property status
    """
    property_status = PropertyStatus.objects.all()
    context = {
        'property_status':property_status
    }

    if request.method == 'GET':

        return render(request, 'deal/Views/add-deal.html', context)
    if request.method =='POST':
        name = request.POST['name']
        print("######## Deal's name is ", name)
       # import pdb
        #pdb.set_trace()
        property_status = request.POST['property_status']
        
        global  deal_data
        def deal_data():
            return property_status, name
        if not name:
            messages.error(request, 'Name is required')
            return render(request, 'deal/Views/add-deal.html', context)

       

        return redirect('address_assets')

data_to_save = None
def address_asset(request):
    sort  = Sort.objects.all()
    property_type = PropertyType.objects.all()
    expand_search_radius = ExpandSearchRadius.objects.all()
    home_size = HomeSize.objects.all()
    in_unit_features = InUnitFeatures.objects.all()
    community_ammenities = CommunityAmmenities.objects.all()
    ok = Ok.objects.all()

    sort_sale = SortSale.objects.all()
    property_type_sale = PropertyTypeSale.objects.all()
    property_type_nyc_only = PropertyTypeNycOnly.objects.all()
    no_hoa_fee = NoHoaFee.objects.all()
    home_size_min_sale = HomeSizeMinSale.objects.all()
    home_size_max_sale = HomeSizeMaxSale.objects.all()
    lot_size = LotSize.objects.all()
    stories = Stories.objects.all()
    garage = Garage.objects.all()
    heating_cooling = HeatingCooling.objects.all()
    inside_rooms = InsideRooms.objects.all()
    outside_features = OutsideFeatures.objects.all()
    lot_views = LotViews.objects.all()
    community_ammenities_sale = CommunityAmmenitiesSale.objects.all()
    features_in_nyc_only = FeaturesInNycOnly.objects.all()


    context = {
        'sort':sort,
        'property_types':property_type,
        'expand_search_radius':expand_search_radius,
        'home_sizes':home_size,
        'in_unit_features':in_unit_features,
        'community_ammenities':community_ammenities,
        'ok':ok,
        'sort_sales':sort_sale,
        'property_type_sales':property_type_sale,
        'property_type_nyc_only':property_type_nyc_only,
        'no_hoa_fees':no_hoa_fee,
        'home_size_min_sales':home_size_min_sale,
        'home_size_max_sales':home_size_max_sale,
        'lot_sizes':lot_size,
        'stories':stories,
        'garages':garage,
        'heating_coolings':heating_cooling,
        'inside_rooms':inside_rooms,
        'outside_features':outside_features,
        'lot_views':lot_views,
        'community_ammenities_sales':community_ammenities_sale,
        'features_in_nyc_only':features_in_nyc_only

    }
    property_status = deal_data()[0]
    print("########## property status is ", property_status)
    if request.method == 'GET':
        
        context['property_status'] = property_status
        
        return render(request, 'deal/Views/address_asset.html', context)
    
    if request.method == 'POST':
        city = request.POST['city']
        state_code = request.POST['state_code']
        location = request.POST['location']
        context['property_status'] = property_status
        
        if not city:
            messages.error(request, 'City is required')
            return render(request, 'deal/Views/address_asset.html', context)
        if not state_code:
            messages.error(request, 'State code is required')
            return render(request, 'deal/Views/address_asset.html', context)
        

        query= request.POST
        query_data = query.copy()
       # print(query_data)
        query_data.pop('csrfmiddlewaretoken')
        d = {k:v.strip('[]') for k,v in query_data.items()}
        print("Data to make API call is : ", d)

       
        name = deal_data()[1]

        

        if property_status == 'Rent':
            #response = property_search_query(url = url_for_rent, query_params=d)
        
            #df = process_query_response(response=response)
            df = pd.read_csv('/Users/home/Documents/GitHub/WhiteCow2/deal/deal_df.csv')
            df = df.where(df.notnull(), None)
           
            df["description"] = df["description"].apply(eval)
            
            df["location"] = df["location"].apply(eval)
           
            

            #import pdb
            #pdb.set_trace()
            context['deals'] = df
            return render(request, 'deal/Views/address_asset.html', context)
        if property_status == 'Sale':
            print("computing Deal......\n")
            response = property_search_query(url = url_for_sale, query_params=d)
            df = process_query_response(response=response)
            #deal_df = pd.read_csv('/Users/home/Documents/GitHub/WhiteCow2/deal/deal_df.csv')
            #df = pd.read_csv('/Users/home/Documents/GitHub/WhiteCow2/sale.csv')
            list_property_id = df['property_id'].tolist()[:3]
            deal_dict = calculate_deal(list_property_id, df)
            
            deal_df = get_deal_datafrane(deal_dict, df)
           
            deal_df = deal_df.where(deal_df.notnull(), None)

            deal_df = formatting(deal_df)
            print("Here is the Deal \n")
            print(deal_df)

            context['deals'] = deal_df
            
           
            property_type = d['property_type']
            context['property_type'] = property_type

           
            global data_to_save
            def data_to_save():
                return name,city,state_code,location, d, deal_df

            context['deals'] = deal_df
            return render(request, 'deal/Views/address_asset.html', context)
            



def save_deal(request):
    data = data_to_save()
    name = data[0]
    city = data[1]
    state_code = data[2]
    location = data[3]
    assets = data[4]
    deal= data[5]
    


    if request.method == 'POST':
        

        Deals.objects.create(name = name,owner=request.user)

        de = Deals.objects.latest('id')
        deal['owner'] = request.user
        deal['deal'] = de

        assets.pop('city')
        assets.pop('state_code')
        assets.pop('location')
        assets['owner'] = request.user
        assets['deal'] =  de
        deal['owner'] = request.user
        deal['deal'] = de
        for k  in assets :
            if assets[k] == '':
                assets[k] = None
        

    
        Adress.objects.create(owner=request.user,deal=de,city=city,state_code=state_code, location=location)
        AssetsForSale.objects.create(**assets)


        entries = []       
    
        for e in deal.T.to_dict().values():

            entries.append(SubscriptionDataForSale(**e))
        SubscriptionDataForSale.objects.bulk_create(entries)
 
            
        
       # SubscriptionDataForSale.objects.bulk_create(entries)

        return redirect('dashboad')


def view_deal_detail(request, pk):

    deal = Deals.objects.get(pk=pk)

    data = SubscriptionDataForSale.objects.filter(deal_id =pk, owner=request.user)

    deal_df = read_frame(data)
    
    context = {
        'deals':deal_df
    }
    return render(request,'deal/Views/deal-detail.html',context )



def deal_delete(request, pk):
    deal_id = Deals.objects.get(owner=request.user).pk
    deal_id.delete()

    return redirect('index')
    
@login_required
def manage_subscriptions(request):
    """
    Thie view is to display the subcriptions(saved deals) a user has made
    """

    #deal = Deals.objects.all()
    return render(request, 'deal/Views/subscriptions.html')


