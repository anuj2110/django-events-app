from django import forms
from django.forms import ModelForm
from .models import Venue


class VenueForm(ModelForm):
    class Meta:
        model = Venue
        fields = ('name', 'address', 'zip_code', 'phone', 'email_address')
        labels = {
            'name':'',
            'address':'',
            'zip_code':'',
            'phone':'',
            'email_address': ''
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter Venue Name'}),
            'address': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter address'}),
            'zip_code': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter Zip Code'}),
            'phone': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter Phone'}),
            'email_address': forms.EmailInput(attrs={'class': 'form-control','placeholder':'Enter Email address'})
        }
