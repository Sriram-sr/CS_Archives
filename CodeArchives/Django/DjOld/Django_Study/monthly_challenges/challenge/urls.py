from django.urls import path
from . import views

urlpatterns = [
    path("",views.index),
    path("<str:month>",views.choose_month,name="mymonth"),
    path("<int:month>",views.choose_month_number)
]