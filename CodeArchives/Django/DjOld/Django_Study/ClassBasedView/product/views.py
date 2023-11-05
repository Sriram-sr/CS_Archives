from django.shortcuts import render
from .models import Product

def show_products(request):
    products = Product.objects.all()
    context = {'products' : products}
    return render(request,"product/index.html",context=context)
    
