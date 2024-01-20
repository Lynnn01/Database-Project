from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Table(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=255, blank=True)
    slot = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    customer = models.ForeignKey(
        User, on_delete=models.CASCADE, default=None, blank=True, null=True
    )
