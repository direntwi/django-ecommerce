from django.db import models
from drfecommerce.authentication.models import User
from drfecommerce.product.models import ProductLine


# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def total_price(self):
        return sum(item.total_price() for item in self.objects.all())

    def __str__(self) -> str:
        return f"Cart of {self.user.username}"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items', blank=True, null=True)
    product_line = models.ForeignKey(ProductLine, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    def total_price(self):
        return self.quantity * self.product_line.price

    def __str__(self):
        return f"{self.quantity} of {self.product_line.product.name} ({self.product_line.sku})"
