from rest_framework import serializers
from .models import (
    Brand,
    Category,
    Product,
    ProductImage,
    ProductLine,
    Attribute,
    AttributeValue,
)


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = "__all__"


class BrandSerializer(serializers.ModelSerializer):

    class Meta:
        model = Brand
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    brand = BrandSerializer()
    category = CategorySerializer()

    class Meta:
        model = Product
        fields = "__all__"


class ProductLineSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = ProductLine
        fields = "__all__"


class ProductImageSerializer(serializers.ModelSerializer):
    product = ProductLineSerializer()

    class Meta:
        model = ProductImage
        fields = "__all__"


class AttributeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Attribute
        fields = "__all__"


class AttributeValueSerializer(serializers.ModelSerializer):
    attribute = AttributeSerializer()

    class Meta:
        model = AttributeValue
        fields = "__all__"
