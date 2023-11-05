from django.urls import path
from sample.views import Firstview

urlpatters = [
    path('/check',Firstview.as_view())
]