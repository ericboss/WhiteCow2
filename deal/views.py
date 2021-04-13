from django.shortcuts import render,redirect
from .models import(Deals, PropertyStatus, Adress,AssetsForRent,Sort,PropertyType,ExpandSearchRadius,
HomeSize, InUnitFeatures,CommunityAmmenities,Ok,SortSale, PropertyTypeSale, PropertyTypeNycOnly, NoHoaFee,
HomeSizeMinSale, HomeSizeMaxSale,LotSize,Stories,Garage,HeatingCooling,InsideRooms,OutsideFeatures,LotViews,CommunityAmmenitiesSale,
FeaturesInNycOnly)
from django.contrib import messages
from .view_method import *
import json,requests

# Create your views here.
def index(request):
    """
    This view is to display the landing page
    """
    return render(request, 'deal/Views/dashboard.html')

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
       
       # import pdb
        #pdb.set_trace()
        property_status = request.POST['property_status']
        
        global  deal_data
        def deal_data():
            return property_status
        if not name:
            messages.error(request, 'Name is required')
            return render(request, 'deal/Views/add-deal.html', context)

       

        return redirect('address_assets')


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
    property_status = deal_data()
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
        query_data.pop('csrfmiddlewaretoken')
        d = {k:v.strip('[]') for k,v in query_data.items()}

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
            response = property_search_query(url = url_for_sale, query_params=d)
            df = process_query_response(response=response)
            ##df = pd.read_csv('/Users/home/Documents/GitHub/WhiteCow2/deal/deal_df.csv')
            #df = pd.read_csv('/Users/home/Documents/GitHub/WhiteCow2/sale.csv')
            list_property_id = df['property_id'].tolist()[:3]
            deal_dict = calculate_deal(list_property_id, df)
            
            deal_df = get_deal_datafrane(deal_dict, df)
           
            deal_df = deal_df.where(deal_df.notnull(), None)

           # deal_df["description"] = deal_df["description"].apply(eval)

            deal_df["description"] = deal_df["description"].apply(json.dumps)
            deal_df["description"] = deal_df["description"].apply(json.loads)

            #deal_df["location"] = deal_df["location"].apply(eval)

            context['deals'] = deal_df
            return render(request, 'deal/Views/address_asset.html', context)
            




