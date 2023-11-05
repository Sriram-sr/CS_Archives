from tkinter import CASCADE
from django.db import models

# Create your models here.

class Author(models.Model):
    firstname = models.CharField(max_length=10)
    lastname = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.firstname} {self.lastname}'

class Book(models.Model):
    title = models.CharField(max_length=100)
    ratings = models.IntegerField() 
    author = models.ForeignKey(Author,name='books',on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}'