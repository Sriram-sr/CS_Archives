from operator import eq
from django.shortcuts import render,redirect
from . import forms
from .models import Prducts
# Create your views here.

def infoFromForms(request):
    form = forms.EmployeeForm()
    empInfo = {'form':form}
    return render(request,'Firstapp/input.html',context = empInfo)

def show_products(request):
    all_products = Prducts.objects.all().values()
    context = {'products' : all_products}
    return render(request,"productShow.html",context=context)
    
def add_page(request):
    return render(request,'Firstapp/add_pr.html')   

def new_add(request):
    name = request.POST['name']
    net = request.POST['net']
    price = request.POST['price']
    new = Prducts(pname=name,pnet=net,pprice=price)
    new.save()

    return redirect('products/')