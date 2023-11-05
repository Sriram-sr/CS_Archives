from django.shortcuts import render
from django.http import JsonResponse
from .models import Employee
# Create your views here.

def employeeView(request):
    obj = {
        'id': 1,
        'name': "Sriram",
        'salary': 20000
    }

    data = Employee.objects.all()
    response = {'employees' : list(data.values('id','name','sal'))}

    return JsonResponse(response)