from drfecommerce.authentication.serializers import UserSerializer
from drfecommerce.product.serializers import ProductLineSerializer
from rest_framework import serializers

from .models import Wishlist


class WishlistSerializer(serializers.ModelSerializer):
    product_line = ProductLineSerializer()
    user = UserSerializer()

    class Meta:
        model = Wishlist
        fields = "__all__"
