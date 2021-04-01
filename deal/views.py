from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView
from .models import Deals, Adress, ComputeDeals, AssetTypes,Item,SubscriptionData,SubscriptionDataForSale
from django import forms
from .forms import DealAddressForm, DealAssetTypeForm, DealComputeDealForm, DealsForm
from django.contrib.auth.decorators import login_required
import logging,traceback
from django.http import HttpResponse
from .config import *
import requests, json
from .view_method import *
from django.contrib.auth.models import User
from django_pandas.io import read_frame

logger = logging.getLogger('django')



def index(request):
    """
    This view is to display the landing page
    """
    return render(request, 'deal/Views/index.html')

get_data = None
def make_query(request):
    if request.method == 'POST':
        form_deal = DealsForm(request.POST)
        form_adress = DealAddressForm(request.POST)
        form_asset = DealAssetTypeForm(request.POST)
        form_compute = DealComputeDealForm(request.POST)
        if form_adress.is_valid() and form_asset.is_valid() and form_compute.is_valid() and form_deal.is_valid():

            #property_status = form_deal.cleaned_data['property_status']

            params1 = request.POST.items()
            params1 = dict(params1)
            params = params1.copy()
            params['limit'] = 20
            params.pop('csrfmiddlewaretoken')
            #params.pop('property_status')
            adress_data = {}
            adress_data['city'] = params['city']
            adress_data['postal_code'] = params['postal_code']
            adress_data['state_code'] = params['state_code']

            computeDeal_data = {}
            computeDeal_data['period'] = params['period']
            computeDeal_data['compare'] = params['compare']
            computeDeal_data['percentage_compare_average_price'] = params['percentage_compare_average_price']
            

            deal_data = {}
            deal_data['name'] = params['name']
            deal_data['property_status'] = params['property_status']
            deal_data['days'] = params['days']
            deal_data['time'] = params['time']

            asset_params = params.copy()
            asset_params.pop('city')
            asset_params.pop('postal_code')
            asset_params.pop('state_code')
            asset_params.pop('period')
            asset_params.pop('compare')

            asset_params.pop('percentage_compare_average_price')
            asset_params.pop('name')
            asset_params.pop('property_status')
            asset_params.pop('days')
            asset_params.pop('time')
            asset_params.pop('limit')


        
            print(params)

            #if property_status == 'For Rent':
           #     url = url_for_rent
           # else:
           #     url = url_for_sale
            query = formatting(property_status=deal_data['property_status'], params=params
                            , period=computeDeal_data['period'], compare=computeDeal_data['compare'],percentage=computeDeal_data['percentage_compare_average_price'])

            query = query.reset_index(drop=True)
          #  print(query['address'].head())
            global get_data
            def get_data():
                return adress_data, asset_params, query, computeDeal_data,deal_data


            return redirect('display')
    else:
        logger.debug('Submit is NOT a post.')

        form_deal = DealsForm()
        form_adress = DealAddressForm()
        form_compute = DealComputeDealForm()
        form_asset = DealAssetTypeForm()
    return render(request, 'deal/Views/deal-form.html', {'adress':form_adress, 'asset':form_asset,'compute':form_compute,'deal':form_deal })
    

display =None
def display_search_query(request):
    data = get_data()
    
    if request.method == 'POST':
        logger.debug('Submit was  a POST.')

        form_deal = DealsForm(request.POST)
        form_adress = DealAddressForm(request.POST)
        form_compute = DealComputeDealForm(request.POST)
        form_asset = DealAssetTypeForm(request.POST)
        if form_adress.is_valid() and form_asset.is_valid() and form_deal.is_valid() and form_compute.is_valid():
            params = request.POST.items()
            params = dict(params)
            params['limit'] = 20
            params.pop('csrfmiddlewaretoken')

            adress_data = {}
            adress_data['city'] = params['city']
            adress_data['postal_code'] = params['postal_code']
            adress_data['state_code'] = params['state_code']

            computeDeal_data = {}
            computeDeal_data['period'] = params['period']
            computeDeal_data['compare'] = params['compare']
            computeDeal_data['percentage_compare_average_price'] = params['percentage_compare_average_price']
            

            deal_data = {}
            deal_data['name'] = params['name']
            deal_data['property_status'] = params['property_status']
            deal_data['days'] = params['days']
            deal_data['time'] = params['time']

            asset_params = params.copy()
            asset_params.pop('city')
            asset_params.pop('postal_code')
            asset_params.pop('state_code')
            asset_params.pop('period')
            asset_params.pop('compare')

            asset_params.pop('percentage_compare_average_price')
            asset_params.pop('name')
            asset_params.pop('property_status')
            asset_params.pop('days')
            asset_params.pop('time')


        
            query = formatting(property_status=deal_data['property_status'], params=params
                            , period=computeDeal_data['period'], compare=computeDeal_data['compare'],percentage=computeDeal_data['percentage_compare_average_price'])

            query = query.reset_index(drop=True)

            global display
            def display():
                return query
    
    else:
        logger.debug('Submit is NOT a post.')
        

        form_deal = DealsForm(initial = data[4])
        form_adress = DealAddressForm(initial = data[0])
        form_compute = DealComputeDealForm(initial = data[3])
        form_asset = DealAssetTypeForm(initial = data[1])
        query= data[2]
    return render(request, 'deal/Views/display2.html', {'query':query,'adress':form_adress, 'asset':form_asset, 'compute':form_compute,'deal':form_deal, 'property_status':data[4]['property_status']})
    

def saveDeal(request):
  
    data = get_data()
    if request.method == 'POST':

        logger.debug('Submit was  a POST.')

        form_deal = DealsForm(request.POST)
        form_adress = DealAddressForm(request.POST)
        form_compute = DealComputeDealForm(request.POST)
        form_asset = DealAssetTypeForm(request.POST)

        if form_adress.is_valid() and form_asset.is_valid() and form_compute.is_valid() and form_deal.is_valid():
            name = form_deal.cleaned_data['name']
            property_status = form_deal.cleaned_data['property_status']
            form_adress.save()
            form_asset.save()
            form_compute.save()
            address = Adress.objects.latest('id')
            asset = AssetTypes.objects.latest('id')
            compute = ComputeDeals.objects.latest('id')
            de = Deals.objects.create(name=name, property_status=property_status, adress=address,assets=asset,computeDeal=compute)
            request.user.Deals.add(de)
            query = data[2]
            query['deal'] = de
            

            entries = []
            print(query.head())
            if property_status == 'For Rent':
                query.drop('price', inplace=True, axis=1)
                for e in query.T.to_dict().values():
                    entries.append(SubscriptionData(**e))
                SubscriptionData.objects.bulk_create(entries)
               # df = pd.DataFrame(list(SubscriptionData.objects.all().values()))

            else:
                for e in query.T.to_dict().values():
                    entries.append(SubscriptionDataForSale(**e))
                SubscriptionDataForSale.objects.bulk_create(entries)
            
            print("deal id is:", de.id)
           # print(df.tail())


            logger.debug(f"Address, asset types, compte parameters was saved.deal {name} was created and added to user(createor)")

            return redirect('subscriptions')
        else:
            logger.debug("Form was invalid. Nothing will be saved.")
    else:
        logger.debug('Submit is NOT a post.')

        form_deal = DealsForm(initial = data[4])
        form_adress = DealAddressForm(initial = data[0])
        form_compute = DealComputeDealForm(initial = data[3])
        form_asset = DealAssetTypeForm(initial = data[1])
    return render(request, 'deal/Views/save_deal.html', {'deal': form_deal,'adress':form_adress, 'compute':form_compute, 'asset':form_asset})
detail_deal = None
def view_deal(request, pk):
    
    deal = Deals.objects.get(pk = pk)
    status = deal.property_status
    if status== 'For Rent':
        data = SubscriptionData.objects.filter(deal_id=pk)
    else:
        data = SubscriptionDataForSale.objects.filter(deal_id=pk)

    df = read_frame(data)
    print(status)
  #  df["address"] = df["address"].str.strip('{}')
    #df["address"] = df["address"].apply(json.loads)  
   
    #df["photos"] = df["photos"].apply(json.dumps) 

    global detail_deal
    def detail_deal():
        return deal
   # print(df['community'])
    
    return render(request, 'deal/Views/viewdeal.html', {'data':df, 'property_status':status})



refresh_data=None
def refresh_deal(request, pk):

    logger.debug("Refresh deal {0}".format(pk))
    deal = Deals.objects.get(pk = pk) 
    address = Adress.objects.get(pk = pk) 
    asset = AssetTypes.objects.get(pk = pk) 
    compute = ComputeDeals.objects.get(pk = pk) 
    if request.method == 'POST':
        logger.debug('Submit was  a POST.')

        form_deal = DealsForm(request.POST)
        form_adress = DealAddressForm(request.POST)
        form_compute = DealComputeDealForm(request.POST)
        form_asset = DealAssetTypeForm(request.POST)
        if form_adress.is_valid() and form_asset.is_valid() and form_compute.is_valid() and form_deal.is_valid():
            if form_adress.is_valid() and form_asset.is_valid() and form_deal.is_valid() and form_compute.is_valid():
                params = request.POST.items()
                params = dict(params)
                params['limit'] = 20
                params.pop('csrfmiddlewaretoken')

                adress_data = {}
                adress_data['city'] = params['city']
                adress_data['postal_code'] = params['postal_code']
                adress_data['state_code'] = params['state_code']

                computeDeal_data = {}
                computeDeal_data['period'] = params['period']
                computeDeal_data['compare'] = params['compare']
                computeDeal_data['percentage_compare_average_price'] = params['percentage_compare_average_price']
            

                deal_data = {}
                deal_data['name'] = params['name']
                deal_data['property_status'] = params['property_status']
                deal_data['days'] = params['days']
                deal_data['time'] = params['time']

                asset_params = params.copy()
                asset_params.pop('city')
                asset_params.pop('postal_code')
                asset_params.pop('state_code')
                asset_params.pop('period')
                asset_params.pop('compare')
 
                asset_params.pop('percentage_compare_average_price')
                asset_params.pop('name')
                asset_params.pop('property_status')
                asset_params.pop('days')
                asset_params.pop('time')


        
                query = formatting(property_status=deal_data['property_status'], params=params
                            , period=computeDeal_data['period'], compare=computeDeal_data['compare'],percentage=computeDeal_data['percentage_compare_average_price'])
                query = query.reset_index(drop=True)
                global refresh_data
                def refresh_data():
                    return query
            
    
    else:
        logger.debug('Submit is NOT a post.')

        form_deal = DealsForm(instance = deal)
        form_adress = DealAddressForm(instance=address)
        form_compute = DealComputeDealForm(instance=compute)
        form_asset = DealAssetTypeForm(instance= asset)
       
        query= None
    return render(request, 'deal/Views/refresh.html', {'query':query,'adress':form_adress, 'asset':form_asset, 'compute':form_compute,'deal':form_deal, 'de':deal.id, 'property_status':deal.property_status})
    
def save_refresh(request, pk):
    deal = Deals.objects.get(pk = pk) 
    address = Adress.objects.get(pk = pk) 
    asset = AssetTypes.objects.get(pk = pk) 
    compute = ComputeDeals.objects.get(pk = pk) 
    deal2 = Deals.objects.filter(pk=pk)
   
    if request.method == 'POST':

        logger.debug('Submit was  a POST.')

        form_deal = DealsForm(request.POST)
        form_adress = DealAddressForm(request.POST)
        form_compute = DealComputeDealForm(request.POST)
        form_asset = DealAssetTypeForm(request.POST)

        if form_adress.is_valid() and form_asset.is_valid() and form_compute.is_valid() and form_deal.is_valid():
            name = form_deal.cleaned_data['name']
            property_status = form_deal.cleaned_data['property_status']
            form_adress.save()
            form_asset.save()
            form_compute.save()
            address = Adress.objects.get(pk = pk)
            asset = AssetTypes.objects.get(pk=pk)
            compute = ComputeDeals.objects.latest('id')
            deal2.update(name=name, property_status=property_status, adress=address,assets=asset,computeDeal=compute)
            if deal.property_status =='For Rent':
                SubscriptionData.objects.filter(deal_id = pk).delete()
            else:
                SubscriptionDataForSale.objects.filter(deal_id = pk).delete()
            

            df = refresh_data()
    
            df['deal'] = deal
            

            entries = []
            if property_status == 'For Rent':
                df.drop('price', inplace=True, axis=1)
                for e in df.T.to_dict().values():
                    entries.append(SubscriptionData(**e))
                SubscriptionData.objects.bulk_create(entries)
               # df = pd.DataFrame(list(SubscriptionData.objects.all().values()))

            else:
                for e in df.T.to_dict().values():
                    entries.append(SubscriptionDataForSale(**e))
                SubscriptionDataForSale.objects.bulk_create(entries)
            return redirect('subscriptions')
        else:
            logger.debug("Form was invalid. Nothing will be saved.")
    else:
        logger.debug('Submit is NOT a post.')
        form_deal = DealsForm(instance = deal)
        form_adress = DealAddressForm(instance=address)
        form_compute = DealComputeDealForm(instance=compute)
        form_asset = DealAssetTypeForm(instance= asset)
       
        query= None
    return render(request, 'deal/Views/save_refresh.html', {'query':query,'adress':form_adress, 'asset':form_asset, 'compute':form_compute,'deal':form_deal, 'de':deal.id})
    
def detail_view_deal(request,pk):

    deal = detail_deal()
    status = deal.property_status
    

    if request.method == 'GET':
     
        if status == 'For Rent':
            data = SubscriptionData.objects.filter(deal_id = deal.pk)
        else:
            data = SubscriptionDataForSale.objects.filter(deal_id = deal.pk)
        data = read_frame(data)
        print(data)
        
        return HttpResponse(data.iloc[pk])
        #render(request, 'deal/detail_deal.html', {'deal':deal.formatting().iloc[pk]})

        
        #return HttpResponse(data.iloc[pk])
        #render(request, 'deal/detail_deal.html', {'deal':deal.formatting().iloc[pk]})
    
    return render(request, 'deal/Views/detail_deal_specific.html', {'data':data})  


def detail_view_refresh(request,pk):

    if request.method == 'GET':
        
        data = refresh_data()
        
        return HttpResponse(data.iloc[pk])
        #render(request, 'deal/detail_deal.html', {'deal':deal.formatting().iloc[pk]})
    
    return render(request, 'deal/detail_refresh.html')




        



@login_required
def manage_subscriptions(request):
    """
    Thie view is to display the subcriptions(saved deals) a user has made
    """
    
    #deal = Deals.objects.all()
    return render(request, 'deal/subscriptions.html')

@login_required      
def edit(request, pk):
    """
    Edit view is to saved deal. The user is presented with a form with instance values corresponding to the data 
    the user saved. The user can edit the form and save. The page will be redirected to the page to view saved subscriptions upon save
    """
    logger.debug("Edit deal {0}".format(pk))
    deal = Deals.objects.get(pk = pk)
    if request.method == 'POST':
        logger.debug('Submit was  a POST.')

        deal_form = DealsForm(request.POST, instance = deal)
        if deal_form.is_valid():
            deal_form.save()
            logger.debug('Deal was saved.')
            return redirect('subscriptions')
        else:
            logger.debug("Form was invalid. Nothing will be saved.")
    else:
        logger.debug('Submit is NOT a post.')

        deal_form = DealsForm( instance=deal)
    return render(request, 'deal/edit.html', {'edit_form':deal_form, 'deal':deal})

@login_required   
def delete(request, pk):
    """
    delete view is to saved deal. The user is presented to delete page upon request. 
    The deal is deleted upon confirmtion. The page will be redirected to the page to view saved subscriptions upon delete
    """
    logger.debug("Delete deal {0}".format(pk))
    deal = Deals.objects.get(pk = pk) 
    if request.method =='POST':
        logger.debug('Submit was  a POST.')

        deal.delete()
        logger.debug('Deal deleted.')

        return redirect('subscriptions')
    return render(request, 'deal/delete.html', {'deal':deal})


   
    

def videos(request):
    obj = Item.objects.all()
    return render(request,'deal/Views/index.html',{'obj':obj})

def detail(request,pk):
    if request.method == 'GET':
        
        data = get_data()[2]
        print (data)
        
        return HttpResponse(data.iloc[pk])
        #render(request, 'deal/detail_deal.html', {'deal':deal.formatting().iloc[pk]})
    
    return render(request, 'deal/detail_deal.html')