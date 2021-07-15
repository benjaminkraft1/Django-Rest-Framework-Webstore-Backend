from django.db import models
from .categories_model import Categories

class Products(models.Model):
    name = models.TextField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.ForeignKey(Categories, null=True, blank=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(null=True, auto_now_add=True)
    updated_at = models.DateTimeField(null=True, auto_now=True)
    

    def __str__(self):
        return self.name
