from carts.models import Cart, CartItem
from rest_framework import serializers


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields ="__all__"
        read_only_fields = ['id']

class CartSerializer(serializers.ModelSerializer):
    cartitems = CartItemSerializer(many=True, read_only=True)
    class Meta:
        model = Cart
        fields =['id','name','created_at','updated_at',
                 'num_of_products','num_of_items','total_price','user','cartitems'
        ]
        read_only_fields = ['id','created_at','updated_at',
                            'num_of_products','num_of_items','total_price','user'
        ]

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)
