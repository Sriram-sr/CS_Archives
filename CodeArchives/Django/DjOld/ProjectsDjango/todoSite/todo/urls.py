from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='todo'),
    path('submit',views.index),
    path('del/<int:id>/',views.delete),
]