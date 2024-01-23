from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Userinfo(models.Model):
    member = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    phone = models.CharField(max_length=10)
    point = models.IntegerField(default=0)

