from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import *
from .serializers import *
from drf_spectacular.utils import extend_schema

# Create your views here.


class CategoryViewSet(viewsets.ViewSet):
    """
    A simple Viewset for viewing all categories
    """

    queryset = Category.objects.all()

    @extend_schema(responses=CategorySerializer)
    def list(self, request):
        serializer = CategorySerializer(self.queryset, many=True)
        return Response(serializer.data)


class BrandViewSet(viewsets.ViewSet):
    """
    A simple Viewset for viewing all brands
    """

    queryset = Brand.objects.all()

    @extend_schema(responses=BrandSerializer)
    def list(self, request):
        serializer = BrandSerializer(self.queryset, many=True)
        return Response(serializer.data)


class ProductViewSet(viewsets.ViewSet):
    """
    A simple Viewset for viewing all products
    """

    queryset = Product.objects.all()

    @extend_schema(responses=ProductSerializer)
    def list(self, request):
        serializer = ProductSerializer(self.queryset, many=True)
        return Response(serializer.data)


class ProductLineViewSet(viewsets.ViewSet):
    """
    A simple Viewset for viewing all product lines
    """

    queryset = ProductLine.objects.all()

    @extend_schema(responses=ProductLineSerializer)
    def list(self, request):
        serializer = ProductLineSerializer(self.queryset, many=True)
        return Response(serializer.data)


class ProductImageViewSet(viewsets.ViewSet):
    """
    A simple Viewset for viewing all product images
    """

    queryset = ProductImage.objects.all()

    @extend_schema(responses=ProductImageSerializer)
    def list(self, request):
        serializer = ProductImageSerializer(self.queryset, many=True)
        return Response(serializer.data)


class AttributeViewSet(viewsets.ViewSet):
    """
    A simple Viewset for viewing all attributes
    """

    queryset = Attribute.objects.all()

    @extend_schema(responses=AttributeSerializer)
    def list(self, request):
        serializer = AttributeSerializer(self.queryset, many=True)
        return Response(serializer.data)


class AttributeValueViewSet(viewsets.ViewSet):
    """
    A simple Viewset for viewing all attributes
    """

    queryset = AttributeValue.objects.all()

    @extend_schema(responses=AttributeValueSerializer)
    def list(self, request):
        serializer = AttributeValueSerializer(self.queryset, many=True)
        return Response(serializer.data)
