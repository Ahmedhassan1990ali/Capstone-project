from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from products.serializers import ProductSerializer, ProductCategorySerializer
from products.permissions import IsAdminOrReadOnly
from products.models import Product, ProductCategory
# Create your views here.

class ProductModelViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class= ProductSerializer
    permission_classes = [IsAdminOrReadOnly]

class ProductCategoryModelViewSet(ModelViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class= ProductCategorySerializer
    permission_classes = [IsAdminOrReadOnly]