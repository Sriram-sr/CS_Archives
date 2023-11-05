from django.shortcuts import render
from .models import Store
from django.http import JsonResponse
from rest_framework import generics
from .serializers import StoreSerializer
# Create your views here.

class StoreView(generics.ListCreateAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer