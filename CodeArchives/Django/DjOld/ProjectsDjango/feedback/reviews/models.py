from django.db import models

# Create your models here.
class Review(models.Model):
    Username = models.CharField(max_length=50)
    place = models.CharField(max_length=100,null=True)
    password = models.CharField(max_length=50)