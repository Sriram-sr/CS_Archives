from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home_page(request):
    # return HttpResponse("<h1>This is a Homepage</h1>")
    return render(request,'home.html',{'name':'Sriram'})

def form_data(request):
    return render(request,'Forms.html')
    
def add(request):  
    val1 = request.POST['num1']
    val2 = request.POST['num2']
    res = int(val1) + int(val2)
    return render(request,'result.html',{"result" : res})    