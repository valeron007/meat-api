from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
# Register your models here.

from .models import User, Product, Order, OrderItem, Category
    
#admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Category)


