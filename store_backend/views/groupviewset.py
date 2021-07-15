from django.contrib.auth.models import Group
from rest_framework import viewsets
from rest_framework import permissions
from ..serializers.group_serializer import GroupSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    # Only Staff has permission
    permission_classes = [permissions.IsAdminUser]