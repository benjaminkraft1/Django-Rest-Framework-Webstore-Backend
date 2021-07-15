from django.contrib import admin
from store_backend.models.categories_model import Categories
from store_backend.models.orders_model import Orders, OrderItem
from store_backend.models.products_model import Products
# Register your models here.
admin.site.register(Categories)
admin.site.register(Orders)
admin.site.register(OrderItem)
admin.site.register(Products)