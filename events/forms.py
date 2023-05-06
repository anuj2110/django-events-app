from django import forms
from django.forms import ModelForm
from .models import Venue,Events

class EventForm(ModelForm):
    class Meta:
        model = Events
        fields = ('name','event_date','venue','manager','attendees','description')
        labels = {
            'name':'',
            'event_date':'YYYY-MM-DD HH:MM:SS',
            'venue':'Venue',
            'manager':'Manager',
            'attendees':'Attendees',
            'description':''
        }
        widgets={
            'name': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Event Name'}),
            'event_date':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Event Date'}),
            'venue':forms.Select(attrs={'class':'form-select'}),
            'manager':forms.Select(attrs={'class':'form-select'}),
            'attendees':forms.SelectMultiple(attrs={'class':'form-control'}),
            'description':forms.Textarea(attrs={'class':'form-control'})
        }


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
