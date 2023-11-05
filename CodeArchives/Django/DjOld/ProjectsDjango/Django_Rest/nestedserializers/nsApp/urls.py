from django.urls import path,include
from . import views

urlpatterns = [
    path('author',views.AuthorListView.as_view()),
    path('author/<int:pk>',views.AuthorDetailView.as_view()),
    path('books',views.BookListView.as_view()),
    path('books/<int:pk>',views.BookDetailView.as_view()),
]