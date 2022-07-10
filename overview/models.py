from django.db import models

# Create your models here.
class Services(models.Model):
    gruppe = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    dauer = models.IntegerField()
    preis = models.IntegerField()


class Bookings(models.Model):
    #service = models.ForeignKey(Services, on_delete=models.CASCADE)
    service = models.CharField(max_length=500)
    vorname = models.CharField(max_length=255)
    nachname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    nummer = models.IntegerField()
    dauer = models.IntegerField()
    preis = models.IntegerField()
    uhrzeit = models.DateTimeField(unique=True)


class Message(models.Model):
    vorname = models.CharField(max_length=255)
    nachname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    thema = models.CharField(max_length=1000)