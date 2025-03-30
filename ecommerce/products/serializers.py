from products.models import Product, ProductCategory
from rest_framework import serializers

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model= Product
        fields = '__all__'
        read_only_fields = ['id']

class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model= ProductCategory
        fields = '__all__'
        read_only_fields = ['id']