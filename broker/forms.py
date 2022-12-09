from django import forms
from .models import Listing, Zipcode, Neighborhood, HomeType, PriceRange


class FilterForm(forms.Form):
    selectedlisting = forms.ModelChoiceField(queryset=Listing.objects.all(), required=False,
                                             label="", empty_label="Show All")



