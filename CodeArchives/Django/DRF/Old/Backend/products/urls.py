from django.urls import path
from . import views

urlpatterns = [
    path('ser/', views.get_products, name='products'),
    # path('prs/', views.using_rest_response, name='resr-response'),

    # using serializers
    path('products/', views.using_serializers, name='using-serializers'),
    path('products/<int:pk>', views.get_single_product, name='single-product'),

    # generics

    path('view/<int:pk>', views.ProductRetrieveView.as_view(), name='view'),
    path('create/', views.ProductCreateView.as_view(), name='create'),
    
    path('meals/', views.show_meals, name='meals'),
]