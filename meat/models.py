from django.db import models
# Create your models here.
from django.db import models
from phone_field import PhoneField
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):        
    phone = PhoneField(blank=True, help_text='Contact phone number', unique=True)
    address = models.CharField(max_length=200, default='')
    username = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.username


class Category(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    order = models.IntegerField()
    
    def __str__(self):
        return self.title

class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    availability = models.BooleanField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
        
    def __str__(self):
        return self.title

class Order(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=250)
    postal_code = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.PROTECT)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity
    
    
