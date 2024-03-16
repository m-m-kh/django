from django.db import models

from order.models import Order


# Create your models here.
class TransactionModel(models.Model):
    id = models.CharField(primary_key=True,max_length=200)
    link = models.CharField(max_length=200)
    status = models.IntegerField(null=True)
    track_id = models.IntegerField(null=True)
    order_id = models.CharField(null=True, max_length=200)
    amount = models.IntegerField()
    # verification_date = models.DateTimeField()
    # payment_date = models.DateTimeField()
    card_no = models.CharField(null=True,max_length=200)
    hashed_card_no = models.CharField(null=True,max_length=200)

    to_order = models.ForeignKey(to=Order, on_delete=models.CASCADE, related_name='transaction')