from rest_framework import serializers
from .models import User, Product, CartItem

class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = User 
        fields = ['id', 'username', 'password', 'email', 'phone']
        
        
class ProductSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Product
        fields = '__all__'
        
        
        
class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=True)
    class Meta(object):
        model = CartItem
        fields = '__all__'         
      
      
class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True)
    class Meta(object):
        model = Cart
        fields = '__all__'    
        
        

            
        
                      