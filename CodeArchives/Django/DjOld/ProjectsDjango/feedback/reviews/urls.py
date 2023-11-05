from django.urls import path
from . import views

urlpatterns = [
    # path('',views.check),
    # path('tq/',views.tq),
    path('',views.ReviewView.as_view()),
    path('tq/',views.ThankyouView.as_view()),
    path('list/',views.ReviewList.as_view())
]