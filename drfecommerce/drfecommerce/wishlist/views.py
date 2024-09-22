from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Wishlist
from .serializers import WishlistSerializer

# Create your views here.


class WishlistViewSet(viewsets.ModelViewSet):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        This method ensures that each user can only see their own wishlist.
        """
        return Wishlist.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        """
        This method is overridden to ensure the wishlist item is created for the logged-in user.
        """
        serializer.save(user=self.request.user)
