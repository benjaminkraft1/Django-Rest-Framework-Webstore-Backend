from rest_framework import viewsets
from rest_framework import permissions
from ..serializers.categories_serializer import CategoriesSerializer
from ..models.categories_model import Categories


class CategoriesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]