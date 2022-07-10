from asyncio.windows_events import NULL
from calendar import weekday
import datetime
from typing import final
from urllib import request
from django.shortcuts import redirect, render

from overview.models import Bookings, Services

services_selected = []
def select_service(request):
    services= Services.objects.all().values()
    context = {
        'services': services,
        'services_selected': services_selected,
    }
    return render(request, 'select_service.html', context)


def add_service(request, id):
    if Services.objects.get(id = id) not in services_selected:
        services_selected.append(Services.objects.get(id = id))
    return redirect(select_service)


def delete_service(request, id):
    services_selected.pop(services_selected.index(Services.objects.get(id = id)))
    return redirect(select_service)


def select_date(request, start=0, days=7, minutes=30):
    week,i,weekday = get_week(start, days, minutes)
    x = list(range(0,i))
    week = remove_times(week)
    context = {
        'x': x,
        'week': week,
        'weekday': weekday,
    }
    return render(request, 'select_date.html', context)


#today: start Tag, days: wie viele anzeigen
def get_week(today, days, minutes=30, h=9):
    week = []
    weekday = []
    for i in range(days):
        day = datetime.datetime.now() + datetime.timedelta(days=today + i)
        time = []
        weekday.append(day.strftime('%A %d,%m'))
        hours = datetime.timedelta(hours=h)
        interval = datetime.timedelta(minutes=minutes)
        i = hours/ interval
        for x in range(int(i)):
            day_start = datetime.datetime(int(day.strftime('%Y')),int(day.strftime('%m')), int(day.strftime("%d")),8)
            time.append((x*interval + day_start)) 
        week.append(time)
    return week,int(i),weekday


def remove_times(week):
    booked = Bookings.objects.values_list('uhrzeit')
    for i,l in enumerate(week):
        for j,k in enumerate(week[i]):
            if datetime.datetime.now()>=datetime.datetime.strptime(str(week[i][j]), '%Y-%m-%d %H:%M:00'):
                week[i][j] = 'x'
            for booking in booked:
                if str(booking[0]).split('+')[0] == str(week[i][j]):
                    week[i][j] = 'x'
    return week

def safe_date(request, datestring):
    return redirect(customer_info, datestring)


def customer_info(request, datestring):
    dauer = 0
    preis = 0
    name = ""
    for service in services_selected:
        dauer = dauer + service.dauer
        preis = preis + service.preis
        name = name + service.name
    context = {
        'datestring': datestring,
        'services_selected': services_selected,
        'dauer': dauer,
        'preis': preis,
        'name':name,
    }
    return render(request, 'customer_info.html', context)

def save_customer_data(request):
    if request.method == 'POST':
        service = request.POST['service']
        vorname = request.POST['vorname']
        nachname = request.POST['nachname']
        email = request.POST['email']
        vorname = request.POST['vorname']
        nummer = request.POST['nummer']
        dauer = request.POST['dauer']
        preis = request.POST['preis']
        time = parse_date(request.POST['date'])
        booked = Bookings(service = service, vorname = vorname, nachname=nachname, email =email , nummer=nummer, dauer=dauer, preis=preis, uhrzeit = time)
        booked.save()
    context = {
        'name': request.POST['vorname'],
    }
    return redirect(thank_you)

def thank_you(request):
    return render(request, 'thank_you.html')

def parse_date(date):
    date = str.upper(date).replace('.', '')
    date = str.upper(date).replace('NOON', '12 PM')
    if ':' in date:
        result = datetime.datetime.strptime(date, '%B %d, %Y, %I:%M %p').strftime('%Y-%m-%d %H:%M')
    else:
        result = datetime.datetime.strptime(date, '%B %d, %Y, %I %p').strftime('%Y-%m-%d %H:%M')
    return result