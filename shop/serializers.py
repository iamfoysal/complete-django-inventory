from rest_framework import serializers
from .models import Product, Category

class ProductSerializer(serializers.ModelSerializer):

    category_name = serializers.CharField(source='category.name')

    class Meta:
        model = Product
        fields = ('id', 'title', 'price', 'stock', 'category_name', 'description', 'image')
