from django.shortcuts import render
import calendar
from calendar import HTMLCalendar
from datetime import datetime
# Create your views here.


def home(request, year = datetime.now().year, month = datetime.now().strftime('%B')):
    month_number = int(list(calendar.month_name).index(month.capitalize()))
    cal = HTMLCalendar().formatmonth(year,month_number)
    return render(request, 'home.html', {'year': year, 'month': month,'month_number':month_number,'calendar':cal})
