from django.db import models

# Create your models here.

class Store(models.Model):
    id = models.IntegerField(primary_key=True)
    product = models.CharField(max_length=30)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10,decimal_places=3)

    def __str__(self):
        return f'{self.product}'

