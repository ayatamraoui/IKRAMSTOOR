from django.db import models

from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(User,null=True, on_delete=models.CASCADE)
    name= models.CharField(max_length=100, null=True)
    email= models.CharField(max_length=100, null=True)
    phone= models.CharField(max_length=100, null=True)
    age= models.CharField(max_length=100, null=True)
    date_created= models.DateTimeField(auto_now_add=True, null=True)
    

    def __str__(self):
        return self.name



class Cat(models.Model):
    name= models.CharField(max_length=100, null=True)
    avatar = models.ImageField( null=True )
    date_created= models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name
    


class Size(models.Model):
    name= models.CharField(max_length=100, null=True)
    def __str__(self):
        return self.name


class Color(models.Model):
    name= models.CharField(max_length=100, null=True)
    def __str__(self):
        return self.name

class Product(models.Model):
    name= models.CharField(max_length=100, null=True) 
    price_per_unit = models.CharField(max_length=100, null=True)
    basic_unit = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=100, null=True)
    avatar = models.ImageField( null=True )
    date_created= models.DateTimeField(auto_now_add=True, null=True)
    sizes = models.ManyToManyField(Size)
    colors = models.ManyToManyField(Color)
    nameCat = models.ForeignKey(Cat,null=True, on_delete=models.CASCADE) 

    def __str__(self):
        return self.name
    


class Order(models.Model):
    STATUS ={
        ('Pending','Pending'),
        ('Delivered','Delivered'),
        ('in progress','in progress'),
        ('out of order','out of order'),
    }

    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    Product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    Color = models.ForeignKey(Color, null=True, on_delete=models.SET_NULL)
    Size = models.ForeignKey(Size, null=True, on_delete=models.SET_NULL)
    date_created= models.DateTimeField(auto_now_add=True, null=True)
    status= models.CharField(max_length=200, null=True, choices=STATUS)

