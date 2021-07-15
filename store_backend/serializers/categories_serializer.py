from rest_framework import serializers
from ..models.categories_model import Categories

class CategoriesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Categories
        fields = ['id', 'category']
