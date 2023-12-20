from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    phone = models.CharField(verbose_name='phone', max_length=30)
    address = models.CharField(max_length = 300, blank=True)
    is_vendor = models.BooleanField(default=False)
    
    
class Product(models.Model):
    vendor =models.ForeignKey(User, on_delete=models.PROTECT)
    name = models.TextField()
    description = models.TextField()
    quantity = models.TextField()

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    date = models.DateTimeField()
    shipping_address = models.CharField(max_length=200)
    rating = models.IntegerField(default=0)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    current_location = models.CharField(max_length=150)
    quantity = models.IntegerField()
    is_fulfilled = models.BooleanField(default=False)
    

    
class CartItem(models.Model):
    cart = models.ForeignKey(User, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.IntegerField(default = False)   
            
    
