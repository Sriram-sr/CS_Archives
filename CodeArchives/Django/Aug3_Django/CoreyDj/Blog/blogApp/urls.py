from django.urls import path
from . import views

urlpatterns = [
    # path('home/', views.home, name='home'),
    path('home/', views.PostListView.as_view(), name='home'), 
    # path('post/<int:pk>', views.PostDetailView.as_view(), name='post'),
    path('post/<int:pk>', views.post, name='post'),
    # path('create/', views.create_post, name='create-post'),
    path('create/', views.PostCreateView.as_view(), name='create-post'),
    path('about/', views.about, name='about'),
]