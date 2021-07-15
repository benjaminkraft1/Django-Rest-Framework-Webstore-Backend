from rest_framework import serializers
from ..models.products_model import Products


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['id', 'name', 'price', 'category_id', 'created_at', 'updated_at']