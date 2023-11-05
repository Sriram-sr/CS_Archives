from dataclasses import fields
from rest_framework import serializers
from .models import Flight,Passenger,Reservation
import re

class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = '__all__'
        
     # this is for custom validatiion of the fields   
    def validate_flightNumber(self,flightNumber):
        if re.match("^[A-Za-z0-9]*$",flightNumber) == None:
            raise serializers.ValidationError("Invalid flight Number")
        return flightNumber    

class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        # fields = ['firstname','lastname']
        fields = '__all__'


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'
