from django.shortcuts import render
from .models import Flight,Passenger,Reservation
from .serializers import FlightSerializer,PassengerSerializer,ReservationSerializer
from rest_framework import viewsets,status
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['POST'])
def find_flights(request):
    flights = Flight.objects.filter(departure=request.data['departure'],arrival=request.data['arrival'],dateofDeparture=request.data['dateofDeparture'])
    serializer = FlightSerializer(flights,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def find_passenger(request):
    passenger =  Passenger.objects.filter(mobile=request.data['mobile'])
    serializer = PassengerSerializer(passenger,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def save_reservation(request):
    flight = Flight.objects.get(id=request.data['flightId'])
    passenger = Passenger()
    passenger.firstname = request.data['firstname']
    passenger.lastname = request.data['lastname']
    passenger.mobile = request.data['mobile']
    passenger.email = request.data['email']
    passenger.save()

    reservation = Reservation()
    reservation.flight = flight
    reservation.passenger = passenger
    reservation.save()

    return Response(status=status.HTTP_201_CREATED)

class FlightViewset(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer

class PassengerViewset(viewsets.ModelViewSet):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer

class ResrvationViewset(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
