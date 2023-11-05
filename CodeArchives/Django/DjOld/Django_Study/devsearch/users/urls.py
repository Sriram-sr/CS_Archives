from django.urls import path
from .views import *

urlpatterns = [
    path('',user_home,name='home'),
    path('login/',login_page,name='login'),
    path('logout/',logout_func,name='logout'),
    path('register/',register,name='register'),
    path('registercheck/',register_check,name='registercheck'),
    path('projects/',projectsView,name='projects'),
    path('project/<str:pk>/',singleProjectView,name='project'),
]