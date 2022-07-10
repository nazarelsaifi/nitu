from email import message
from urllib import request
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from overview.models import Bookings, Services, Message
from django.urls import reverse

# Create your views here.
def overview(request):

    if request.method == "POST":
        service = Services(gruppe = request.POST['gruppe'], name = request.POST['name'], dauer = request.POST['dauer'], preis = request.POST['preis'])
        service.save()

    services= Services.objects.all().values()
    bookings= Bookings.objects.all().values()
    messages= Message.objects.all().values()

    context = {
        'services': services,
        'bookings': bookings,
        'messages': messages,
    }
    return render(request, 'overview.html', context)


def deleteService(request, id):
    service = Services.objects.get(id = id)
    service.delete()

    return redirect(overview)

def deleteBooking(request, id):
    bookings = Bookings.objects.get(id = id)
    bookings.delete()

    return redirect(overview)

def website(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def location(request):
    return render(request, 'location.html')


def customer_message(request):

    if request.method == "POST":
        vorname = request.POST['firstname']
        nachname = request.POST['lastname']
        email = request.POST['email']
        subject = request.POST['subject']
        message = Message(vorname = vorname, nachname= nachname,email=email,thema=subject)
        print("hallo")
        message.save()
    return render(request, "we_will_contact_you.html")


def delete_customer_message(request,id):
    message = Message.objects.get(id = id)
    message.delete()
    return redirect(overview)