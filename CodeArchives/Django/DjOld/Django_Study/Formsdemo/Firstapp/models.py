from django.db import models

# Create your models here.

class Prducts(models.Model):
    pname = models.CharField(max_length=200)
    pnet = models.IntegerField()
    pprice = models.IntegerField()