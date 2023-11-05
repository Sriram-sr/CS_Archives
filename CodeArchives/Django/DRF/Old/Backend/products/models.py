from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=99.99)

    def __str__(self):
        return self.title

class Meals(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2,null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name