from django.db import models
from django.contrib.auth import get_user_model

from products.models import Product


# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='orders')
    is_paid = models.BooleanField(default=False)

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=700)
    total_price = models.PositiveIntegerField()

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'order {self.pk}'

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_items')
    quantity = models.PositiveIntegerField(default=1)
    price = models.PositiveIntegerField()

    def __str__(self):
        return f'Orde'