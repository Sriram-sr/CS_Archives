from itertools import count
from tabnanny import verbose
from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
# Create your models here.

class Country(models.Model):
   county = models.CharField(max_length=50)
   city = models.CharField(max_length=50)

   class Meta:
      verbose_name_plural = "Countries"

   def __str__(self):
      return f"{self.county}-{self.city}"

class Address(models.Model): # one author can use only one address beacause one to one
    country = models.CharField(max_length=200)
    code = models.CharField(max_length=200)
# giving one to one relationship with address and author 

    def __str__(self):
       return f"Address of {self.country}"

    class Meta: # meta classes is for adding external configurations to objects
       verbose_name_plural = "Address Entries" # by adding this, in admin page this name will be displayed\
       # instead of class name

class Author(models.Model):
   first_name = models.CharField(max_length=100)
   last_name = models.CharField(max_length=100)
   address = models.OneToOneField(Address,on_delete=models.CASCADE,null=True)

   def fullname(self):
      return f"{self.first_name} {self.last_name}"

   def __str__(self):
      return self.fullname()


class Book(models.Model):
    title = models.CharField(max_length=150)
    rating = models.IntegerField(
       validators = [MinValueValidator(1),MaxValueValidator(5)])
    author = models.ForeignKey(Author,on_delete=models.CASCADE,null=True) # cascade makes that if author\
    # deleted book also get deleted
    is_Bestselling = models.BooleanField(default=False) 
    published_countries = models.ManyToManyField(Country)

    def __str__(self):
       return f"{self.title}"