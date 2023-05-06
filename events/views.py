from django.shortcuts import render, redirect
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from .models import Events, Venue
from .forms import VenueForm, EventForm
from django.http import HttpResponseRedirect, HttpResponse
import csv
# Create your views here.


def venue_csv_file(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=venues.csv'
    venues = Venue.objects.all()
    writer = csv.writer(response)
    writer.writerow(['Venue Name', 'Address', 'Zip Code',
                    'Venu Phone', 'Venue Web', 'Venue Email Adress'])
    for venue in venues:
        writer.writerow([venue.name, venue.address, venue.zip_code,
                        venue.phone, venue.web, venue.email_address])
    return response


def venue_text_file(request):
    response = HttpResponse(content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename=venues.txt'
    venues = Venue.objects.all()
    lines = []
    for venue in venues:
        lines.append(
            f'{venue.name}\n{venue.address}\n{venue.zip_code}\n{venue.phone}\n{venue.web}\n{venue.email_address}\n\n\n')
    response.writelines(lines)
    return response


def delete_venue(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    venue.delete()
    return redirect('list-venues')


def delete_event(request, event_id):
    event = Events.objects.get(pk=event_id)
    event.delete()
    return redirect('list-events')


def update_event(request, event_id):
    event = Events.objects.get(pk=event_id)
    form = EventForm(request.POST or None, instance=event)
    if form.is_valid():
        form.save()
        return redirect('list-events')
    return render(request, 'events/update_event.html', {'form': form})


def add_event(request):
    submitted = False
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_event?submitted=True')
    else:
        form = EventForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'events/add_event.html', {'submitted': submitted, 'form': form})


def update_venue(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    form = VenueForm(request.POST or None, instance=venue)
    if form.is_valid():
        form.save()
        return redirect('list-venues')
    return render(request, 'events/update-venue.html', {'form': form})


def search_venues(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        venues = Venue.objects.filter(name__contains=searched)
        print(venues)
        return render(request, 'events/search-venues.html', {'searched': searched, 'venues': venues})
    else:
        return render(request, 'events/search-venues.html', {})


def show_venue(request, venue_id):
    venue = Venue.objects.get(id=venue_id)
    return render(request, 'events/show-venue.html', {'venue': venue})


def list_venues(request):
    venues = Venue.objects.all()
    return render(request, 'events/list-venues.html', {'venues': venues})


def add_venue(request):
    submitted = False
    if request.method == 'POST':
        form = VenueForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_venue?submitted=True')
    else:
        form = VenueForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'events/add_venue.html', {'form': form, 'submitted': submitted})


def list_events(request):
    events_list = Events.objects.all()
    return render(request, 'events/list-events.html', {'events_list': events_list})


def home(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
    month_number = int(list(calendar.month_name).index(month.capitalize()))
    cal = HTMLCalendar().formatmonth(year, month_number)
    return render(request, 'events/home.html', {'year': year, 'month': month, 'month_number': month_number, 'calendar': cal})
