from rest_framework import serializers
from .models import Product, User, Category, Order, OrderItem

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItem()
    
    class Meta:
        model = Order
        fields = ['id', 'first_name', 'last_name', 
                  'email', 'address', 'postal_code',
                  'city', 'created', 'updated', 'paid',
                  'items'
                  ]

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title', 'description', 'order']

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'price', 'availability', 'category']
        
class UserSerializer(serializers.HyperlinkedModelSerializer):        
    def validate(self, attrs):
        if not attrs['phone']:
            raise serializers.ValidationError({"phone": "Phone not fill."})
        return attrs
    
    class Meta:
        model = User
        fields = ['username', 'phone', 'address']

class OrderItemSerializer(serializers.ModelSerializer):    
    product = ProductSerializer()
    
    class Meta:
        model = OrderItem
        fields = ['id', 'price', 'quantity', 'product']

