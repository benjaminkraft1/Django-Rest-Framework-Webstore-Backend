from django.db import models
from django.contrib.auth.models import User
from .products_model import Products


class OrderItem(models.Model):
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

class Orders(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    complete = models.BooleanField(default=False)
    items = models.ManyToManyField(OrderItem)
    created_at = models.DateTimeField(null=True, auto_now_add=True)
    updated_at = models.DateTimeField(null=True, auto_now=True)

    
