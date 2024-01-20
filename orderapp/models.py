from django.db import models
from django.contrib.auth.models import User
from tablesapp.models import Table

# Create your models here.


class Order(models.Model):
    duration = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    table = models.ForeignKey(Table, on_delete=models.CASCADE, default=None)


class OrderDetail(models.Model):
    product = models.CharField(max_length=255)
    discount = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, default=None)

    def sub_total(self):
        return (self.price * self.order.duration) - self.discount
