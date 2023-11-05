from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.

def display_from_template(request):
    return render(request,'demoApp/First_template.html') # referring to Templates folder's html page