from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from .serializers import TodoSerializer

class createView(CreateAPIView):
    serializer_class = TodoSerializer

    def post(self):
        serializer = 

