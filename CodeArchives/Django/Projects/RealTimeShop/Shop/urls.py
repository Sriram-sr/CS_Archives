from django.contrib import admin
from django.urls import path
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register', user_views.register, name='register'),
    path('login/', user_views.login_user, name='login'),
    path('home/', user_views.home, name='home'),
]
