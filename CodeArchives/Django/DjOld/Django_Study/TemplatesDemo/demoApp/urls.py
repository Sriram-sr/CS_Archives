from django.contrib import admin
from django.urls import path
from demoApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('display',views.display_from_template)
]