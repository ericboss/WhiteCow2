from django.shortcuts import render,redirect
from .models import Deals,PropertyStatus
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
    if request.method == 'GET':
        return render(request, 'deal/Views/address_asset.html')
    
    if request.method == 'POST':
        city = request.POST['city']
        state_code = request.POST['state_code']
        location = request.POST['location']
        
        if not city:
            messages.error(request, 'City is required')
            return render(request, 'deal/Views/address_asset.html')
        if not state_code:
            messages.error(request, 'State code is required')
            return render(request, 'deal/Views/address_asset.html')

