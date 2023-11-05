from django.shortcuts import render
from django.http import JsonResponse

def home(request):
    context = {
        'Name': 'Sriram',
        'Age': 22
    }

    return JsonResponse(context)