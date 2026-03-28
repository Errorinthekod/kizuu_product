from rest_framework import serializers
from .models import Product, Category, User




class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id',
                  'username',
                  'email']
        extra_kwargs = {'password': {'write_only': True}}



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
