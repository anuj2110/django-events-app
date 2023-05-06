from django.shortcuts import render
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from .models import Events,Venue
from .forms import VenueForm
from django.http import HttpResponseRedirect
# Create your views here.


def show_venue(request,venue_id):
    venue = Venue.objects.get(id = venue_id)
    return render(request,'events/show-venue.html',{'venue':venue})
def list_venues(request):
    venues = Venue.objects.all()
    return render(request,'events/list-venues.html',{'venues':venues})
def add_venue(request):
    submitted = False
    if request.method=='POST':
        form = VenueForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_venue?submitted=True')
    else:
        form = VenueForm
        if 'submitted' in request.GET:
            submitted = True
        
    return render(request,'events/add_venue.html',{'form':form,'submitted':submitted})
def list_events(request):
    events_list = Events.objects.all()
    return render(request,'events/list-events.html',{'events_list':events_list})
def home(request, year = datetime.now().year, month = datetime.now().strftime('%B')):
    month_number = int(list(calendar.month_name).index(month.capitalize()))
    cal = HTMLCalendar().formatmonth(year,month_number)
    return render(request, 'events/home.html', {'year': year, 'month': month,'month_number':month_number,'calendar':cal})
