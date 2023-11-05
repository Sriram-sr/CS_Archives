from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=30)
    mobile = models.CharField(max_length=12, null=True)
    email = models.CharField(max_length=30, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.name           

class Product(models.Model):
    CATEGORY = (
        ('Indoor','Indoor'),
        ('Outdoor','Outdoor')
    )
    name = models.CharField(max_length=100)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=100, null=True, choices=CATEGORY)
    description = models.CharField(max_length=200, null=True, blank=True) 
    date_created = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag,null=True)

    def __str__(self):
        return self.name  

class Order(models.Model):
    STATUS = (
        ('Pending','Pending'),
        ('Out for delivery','Out for delivery'),
        ('Delivered','Delivered')
    )
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    status = models.CharField(max_length=100, choices=STATUS)
    note = models.CharField(max_length=100,null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.customer)
