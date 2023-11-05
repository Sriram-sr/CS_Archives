from django.db import models

class Product(models.Model):
    sno = models.IntegerField()
    pname = models.CharField(max_length=200)
    quantity = models.IntegerField()
        
