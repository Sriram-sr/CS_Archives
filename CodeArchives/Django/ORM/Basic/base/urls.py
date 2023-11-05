from django.urls import path
from . import views, custom_view

urlpatterns = [
    path('', views.using_order_by, name='onlyviews'),
]