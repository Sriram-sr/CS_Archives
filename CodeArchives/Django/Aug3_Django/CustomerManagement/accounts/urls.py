from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.homepage,name='homepage'),
    path('register/', views.register, name='register' ),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('products/',views.products,name='products'),
    c
    path('customers/<int:pk>',views.customers,name='customers'),
    path('createorder/<int:pk>',views.CreateOrder,name='createorder'),
    path('updateorder/<int:pk>',views.updateOrder,name='updateorder'),
    path('deleteorder/<int:pk>',views.deleteOrder,name='deleteorder'),
]