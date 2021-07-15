from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions
from ..serializers.orders_serializer import OrdersSerializer
from ..models.orders_model import Orders


class OrdersViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows orders to be viewed or edited.
    """
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer
    permission_classes = [permissions.DjangoModelPermissions]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['complete', 'user']

    def get_queryset(self):
        """
        This view should return orders for the currently authenticated user only.
        """
        user = self.request.user

        if user.is_staff:
            # Don't apply a filter for Staff User
            return Orders.objects.all()
        else:
            # Show only Orders that belong to a user
            return Orders.objects.filter(user=user)

