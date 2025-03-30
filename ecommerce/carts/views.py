from django.shortcuts import render
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from carts.serializers import CartSerializer, CartItemSerializer
from carts.models import Cart,CartItem
from carts.permissions import IsOwnerOfCart 
from rest_framework import filters
from rest_framework.exceptions import PermissionDenied
# Create your views here.

class UserCartsModelViewSet(ModelViewSet):
    permission_classes =[IsAuthenticated]
    serializer_class = CartSerializer
    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user).order_by("-updated_at")
    
class UserCartItemsModelViewSet(ModelViewSet):
    permission_classes =[IsAuthenticated, IsOwnerOfCart]
    serializer_class = CartItemSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['id','cart__id','product__name']

    def get_queryset(self):
        return CartItem.objects.filter(cart__user=self.request.user).order_by("-id")
    
    def perform_create(self, serializer):
        cart = serializer.validated_data.get('cart')
        if cart.user != self.request.user:
            raise PermissionDenied("You can only add items to your own cart.")
        serializer.save()
    
class AdminCartsModelViewSet(ReadOnlyModelViewSet):
    permission_classes =[IsAdminUser]
    serializer_class = CartSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['id','name','user__email']

    def get_queryset(self):
        return Cart.objects.all().order_by("-id")

class AdminCartItemsModelViewSet(ReadOnlyModelViewSet):
    permission_classes =[IsAdminUser]
    serializer_class = CartItemSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['id','cart__id','product__name']

    def get_queryset(self):
        return CartItem.objects.all().order_by("-id")
    


