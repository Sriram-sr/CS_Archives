from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.login_page,name='login'),
    path('logout/',views.logout_page,name='logout'),
    path('register/',views.register_page,name='register'),
    path('profile/<int:pk>',views.userprofile,name='user-profile'),
    path('',views.home,name='home'),
    path('room/<int:pk>/',views.room,name='room'),
    path('create/',views.createroom,name='create-room'),
    path('update/<str:pk>/',views.updateroom,name='update'),
    path('delete/<str:pk>',views.deleteroom,name='delete'),
    path('deletemsg/<str:pk>',views.delete_message,name='delete-message'),
    path('updateProfile/',views.updateprofile,name='update-profile'),
    path('topics/',views.topicsList,name='topics'),
]