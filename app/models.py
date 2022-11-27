from django.db import models


class Product(models.Model) :

    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(max_length=1000)
    size = models.TextField(max_length=1000, null=True)
    circumference = models.TextField(max_length=1000, null=True)
    weight = models.TextField(max_length=1000,null=True)
    image = models.ImageField(upload_to='uploads')
    image1 = models.ImageField(upload_to='uploads', null=True)
    image2 = models.ImageField(upload_to='uploads', null=True)
    image3 = models.ImageField(upload_to='uploads', null=True)
    
class Comments(models.Model) :

    name = models.CharField(max_length=100)
    comment = models.TextField(max_length=1000)
    issued = models.DateTimeField(null=True)
    
    
    
