from django.forms import ModelForm
from .models import Adress, AssetTypes, ComputeDeals, Deals


class DealAddressForm(ModelForm):
    """
    Address form
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['city'].widget.attrs.update({'class': 'form-control days'})
        self.fields['state_code'].widget.attrs.update(
            {'class': 'form-control time'})
        self.fields['postal_code'].widget.attrs.update(
            {'class': 'form-control time'})

        self.fields['city'].widget.attrs['placeholder'] = 'Enter city'
        self.fields['state_code'].widget.attrs['placeholder'] = 'state code'
        self.fields['postal_code'].widget.attrs['placeholder'] = 'postal code'

        self.fields['city'].label = ''
        self.fields['state_code'].label = ''
        self.fields['postal_code'].label = ''

    class Meta:
        model = Adress
        fields = ['city', 'state_code', 'postal_code']


class DealComputeDealForm(ModelForm):
    """
    Compute deals form
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['period'].widget.attrs.update(
            {'class': 'form-control days'})
        self.fields['compare'].widget.attrs.update(
            {'class': 'form-control time'})
        self.fields['percentage_compare_average_price'].widget.attrs.update(
            {'class': 'form-control time'})

        self.fields['period'].widget.attrs['placeholder'] = 'Period'
        self.fields['compare'].widget.attrs['placeholder'] = 'Compare'
        self.fields['percentage_compare_average_price'].widget.attrs['placeholder'] = ' % average price'

        self.fields['period'].label = ''
        self.fields['compare'].label = ''
        self.fields['percentage_compare_average_price'].label = ''

    class Meta:
        model = ComputeDeals
        fields = ['period', 'compare', 'percentage_compare_average_price']


class DealAssetTypeForm(ModelForm):
    """
    Assets type form
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['baths_min'].widget.attrs.update(
            {'class': 'form-control days'})
        self.fields['beds_min'].widget.attrs.update(
            {'class': 'form-control time'})
        self.fields['radius'].widget.attrs.update(
            {'class': 'form-control time'})

        self.fields['baths_min'].widget.attrs['placeholder'] = 'min baths'
        self.fields['beds_min'].widget.attrs['placeholder'] = 'min beds'
        self.fields['radius'].widget.attrs['placeholder'] = 'Radius'

        self.fields['baths_min'].label = ''
        self.fields['beds_min'].label = ''
        self.fields['radius'].label = ''

    class Meta:
        model = AssetTypes
        fields = ['baths_min', 'beds_min', 'radius']


class DealsForm(ModelForm):
    """
    Deals form
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control name'})
        self.fields['property_status'].widget.attrs.update(
            {'class': 'form-control property_status'})
        self.fields['days'].widget.attrs.update({'class': 'form-control days'})
        self.fields['time'].widget.attrs.update({'class': 'form-control time'})

        self.fields['name'].widget.attrs['placeholder'] = 'Enter deal name'

        self.fields['name'].label = ''
        self.fields['time'].label = ''
        self.fields['property_status'].label = ''
        self.fields['days'].label = ''

    class Meta:
        model = Deals
        fields = ['name', 'property_status', 'days', 'time']
