from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions
from ..serializers.products_serializer import ProductsSerializer
from ..models.products_model import Products


class ProductsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Products.objects.all().order_by('name')
    serializer_class = ProductsSerializer
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'category_id']
