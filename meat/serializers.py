from rest_framework import serializers
from .models import Product, User, Category, Order, OrderItem
# Сериализатор модели Product
class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'price', 'availability', 'category']

# Сериализатор модели OrderItem
class OrderItemSerializer(serializers.HyperlinkedModelSerializer):    
    product = ProductSerializer()
    
    class Meta:
        model = OrderItem
        fields = ['id', 'price', 'quantity', 'product']
        
# Сериализатор модели Order
class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)
    
    class Meta:
        model = Order
        fields = ['id', 'first_name', 'last_name', 
                  'email', 'address', 'postal_code',
                  'city', 'created', 'updated', 'paid',
                   'total', 'user', 'items',
                  ]        
    
    def create(self, validated_data):        
        items = validated_data.pop('items')
        order = Order.objects.create(**validated_data)        
        
        for item in items:                        
            product, createt = Product.objects.get_or_create(**item['product'])
            item['product'] = product                        
            OrderItem.objects.create(order=order, **item)
        
        order.set_total()
        return order

# Сериализатор модели Category
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title', 'description', 'order']

# Сериализатор модели User
class UserSerializer(serializers.HyperlinkedModelSerializer):        
    def validate(self, attrs):
        if not attrs['phone']:
            raise serializers.ValidationError({"phone": "Phone not fill."})
        return attrs
    
    class Meta:
        model = User
        fields = ['username', 'phone', 'address']
