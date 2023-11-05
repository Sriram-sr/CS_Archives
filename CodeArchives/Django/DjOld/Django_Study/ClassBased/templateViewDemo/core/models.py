from django.db import models

class AllProducts(models.Model):
    pname = models.CharField(max_length=100)
    pquant = models.IntegerField()
    pprice = models.IntegerField()

    
