from django.shortcuts import render
from .models import Meals, Product
from django.forms.models import model_to_dict
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from .serializers import ProductSerializer, MealSerializer

def get_products(request):
    products = Product.objects.all().order_by('price').last()
    product_Json = model_to_dict(products)

    return JsonResponse(product_Json)

@api_view(['GET', 'POST'])
def using_rest_response(request):
    all_products = Product.objects.all().first()
    all_products = model_to_dict(all_products)
    return Response(all_products)

# the above apis is just for response sending, below is the real model api    

@api_view(['GET', 'POST'])
def using_serializers(request):
    if request.method == 'POST':
        received_data = ProductSerializer(data=request.data)
        if received_data.is_valid():
            received_data.save()
            print('data stored')

    products = Product.objects.all()
    seralized_data = ProductSerializer(products, many=True)
    
    return Response(seralized_data.data)

@api_view(['GET'])
def get_single_product(request, pk):
    product = Product.objects.get(id=pk)
    serialized_data = ProductSerializer(product)

    return Response(serialized_data.data)
# using generics    
# retreive api view is for retrieving single object data

class ProductRetrieveView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductCreateView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

@api_view(['GET', 'POST'])
def show_meals(request):
    if request.method == 'POST':
        serializer = MealSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print('Meal Saved')

    meals = Meals.objects.all()
    serializer = MealSerializer(meals, many=True)
    return Response(serializer.data)

