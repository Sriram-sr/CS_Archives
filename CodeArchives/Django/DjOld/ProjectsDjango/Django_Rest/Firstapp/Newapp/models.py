from django.db import models

# Create your models here.

class Employee(models.Model):
    s_no = models.IntegerField()
    name = models.CharField(max_length=20)
    sal = models.IntegerField()

    def __str__(self):
        return f"{self.name}"