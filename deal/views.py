from django.shortcuts import render,redirect
from .models import(Deals, PropertyStatus, Adress,AssetsForRent,Sort,PropertyType,ExpandSearchRadius,
HomeSize, InUnitFeatures,CommunityAmmenities,Ok)
from django.contrib import messages

# Create your views here.
def index(request):
    """
    This view is to display the landing page
    """
    return render(request, 'deal/Views/dashboard.html')


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
        property_status = request.POST['property_status']
        
        if not name:
            messages.error(request, 'Name is required')
            return render(request, 'deal/Views/add-deal.html', context)

        #import pdb
        #pdb.set_trace()

        return redirect('address_assets')


def address_asset(request):
    sort  = Sort.objects.all()
    property_type = PropertyType.objects.all()
    expand_search_radius = ExpandSearchRadius.objects.all()
    home_size = HomeSize.objects.all()
    in_unit_features = InUnitFeatures.objects.all()
    community_ammenities = CommunityAmmenities.objects.all()
    ok = Ok.objects.all()

    context = {
        'sort':sort,
        'property_types':property_type,
        'expand_search_radius':expand_search_radius,
        'home_sizes':home_size,
        'in_unit_features':in_unit_features,
        'community_ammenities':community_ammenities,
        'ok':ok
    }

    if request.method == 'GET':
        return render(request, 'deal/Views/address_asset.html', context)
    
    if request.method == 'POST':
        city = request.POST['city']
        state_code = request.POST['state_code']
        location = request.POST['location']
        
        if not city:
            messages.error(request, 'City is required')
            return render(request, 'deal/Views/address_asset.html', context)
        if not state_code:
            messages.error(request, 'State code is required')
            return render(request, 'deal/Views/address_asset.html', context)

