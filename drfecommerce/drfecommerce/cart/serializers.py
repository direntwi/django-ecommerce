from drfecommerce.product.models import ProductLine
from rest_framework import serializers

from .models import Cart, CartItem

# class CartSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Cart
#         fields = ['id', 'created_at']

# class CartItemSerializer():
#     class Meta:
#         model = CartItem

class CartItemSerializer(serializers.ModelSerializer):
    product_line = serializers.StringRelatedField(read_only=True)
    product_line_id = serializers.PrimaryKeyRelatedField(queryset=ProductLine.objects.all(), source='product_line')

    class Meta:
        model = CartItem
        fields = "__all__"

class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)
    total_price = serializers.ReadOnlyField()

    class Meta:
        model = Cart
        fields = ['id', 'user', 'items', 'total_price', 'created_at', 'updated_at']


