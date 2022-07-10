from faulthandler import disable
from math import trunc
from django.shortcuts import redirect, render
from overview.models import Bookings, Services
import datetime

auswahl= []
datum = []
date_text = []
dis = []
# Create your views here.
def oldbooking(request):
    services= Services.objects.all().values()
    booked = Bookings.objects.all().values()

    if request.method == 'POST':
        booked = Bookings(customerName = request.POST['customerName'], email = request.POST['email'], time = request.POST['date'])
        booked.save()
        return render(request, 'thanks.html')


    days = 7
    week = {}
    for i in range(days):
        day = datetime.datetime.now() + datetime.timedelta(days=i)
        week[day.strftime("%A")] = {
            'day': day.strftime("%d"),
            'month': day.strftime("%m"),
            'year': day.strftime("%Y"),
        }
            

    time = []
    hours = datetime.timedelta(hours=9)
    interval = datetime.timedelta(minutes=30)
    i = hours/ interval
    for x in range(int(i)):
        day = datetime.datetime.now()
        day_start = datetime.datetime(int(day.strftime('%Y')),int(day.strftime('%m')), int(day.strftime("%d")),8)
        time.append((x*interval + day_start).strftime("%X")) 
    

    context = {
        'services': services,
        'week': week,
        'time': time,
        'auswahl': auswahl,
        'datum': datum,
        'date_text': date_text,
        'dis': dis,
    }
    return render(request, 'booking.html', context)


def service(request,service):
    if Services.objects.get(id = service) not in auswahl:
        auswahl.append(Services.objects.get(id = service))
    return redirect(booking)

def deleteS(request, service):
    auswahl.pop(auswahl.index(Services.objects.get(id = service)))
    return redirect(booking)

def date(request, year, month, day, time):
    if len(datum) > 0:
        datum.pop()
    if len(date_text) > 0:
        date_text.pop()
    dlist = Bookings.objects.values_list('time')
    for d in  dlist:

        if str(d[0]).split('+')[0] == str(datetime.datetime(int(year), int(month), int(day), int(time.split(':')[0]), int(time.split(':')[1]))) :
            date_text.append("termin nicht verfuegbar") 
            dis.append('disabled')
            return redirect(booking)
    if len(dis) > 0:
        dis.pop()
    datum.append("{}-{}-{}T{}".format(str(year), str(month), str(day), str(time)))
    return redirect(booking)


    """path('booking/', booking, name='booking'),
    path('booking/<int:service>', service),
    path('booking/<int:year>/<int:month>/<int:day>/<str:time>', date),
    path('booking/deleteS/<int:service>', deleteS),"""