from rest_framework import serializers
from ..models.orders_model import Orders


class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = ['id', 'user', 'items', 'complete', 'created_at', 'updated_at']