from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    money = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    item = models.ManyToManyField("Item")


class Case(models.Model):
    name = models.CharField(max_length=50)
    item_list = models.ManyToManyField("Item")
    price = models.DecimalField(max_digits=5, decimal_places=2)


class Item(models.Model):
    name = models.CharField(max_length=256)
    value = models.DecimalField(max_digits=3, decimal_places=2)

