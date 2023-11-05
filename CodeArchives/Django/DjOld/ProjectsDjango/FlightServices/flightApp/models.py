from ast import Pass
from django.db import models

# Create your models here.
class Flight(models.Model):
    flightNumber = models.CharField(max_length=20)
    flightName = models.CharField(max_length=20)
    departure = models.CharField(max_length=20)
    arrival = models.CharField(max_length=20)
    dateofDeparture = models.DateField()
    estimatedTime = models.TimeField()

class Passenger(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    mobile  = models.CharField(max_length=10)

class Reservation(models.Model):
    flight = models.ForeignKey(Flight,on_delete=models.CASCADE)
    passenger = models.OneToOneField(Passenger,on_delete=models.CASCADE)    