from enum import unique
from operator import mod
from django.db import models
from drfecommerce.authentication.models import User
from drfecommerce.product.models import ProductLine
# Create your models here.


class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    product_line = models.ForeignKey(ProductLine, on_delete=models.CASCADE, blank=True, null=True)
    added_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ("user", "product_line")
    
    def __str__(self):
        return f"{self.user.username}'s wishlist item: {self.product_line.product.name}"


