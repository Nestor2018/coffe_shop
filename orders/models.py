from django.db import models
from django.contrib.auth.models import User

from products.models import Product


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    order_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"order{self.id} by {self.user}"


class OrderProduct(models.Model):
    orden = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.orden} - {self.product} - {self.quantity}"
