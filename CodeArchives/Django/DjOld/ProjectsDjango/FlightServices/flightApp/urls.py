from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('flights',views.FlightViewset)
router.register('passengers',views.PassengerViewset)
router.register('reservations',views.ResrvationViewset)
urlpatterns = [
    path('',include(router.urls)),
    path('findflights/',views.find_flights),
    path('passenger/',views.find_passenger),
    path('save/',views.save_reservation)
]