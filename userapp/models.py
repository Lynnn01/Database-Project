from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Point(models.Model):
    member = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    point = models.IntegerField(default=0)

