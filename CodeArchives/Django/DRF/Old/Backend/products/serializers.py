from .models import Product, Meals
from rest_framework import serializers

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meals
        fields = '__all__'
