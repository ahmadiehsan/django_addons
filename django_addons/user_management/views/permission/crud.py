from django.contrib.auth.models import Permission
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from django_addons.user_management.options.opts import USER_MANAGEMENT_OPTIONS
from django_addons.user_management.serializers.permission.crud import PermissionCRUDSerializer


class PermissionCRUDView(mixins.RetrieveModelMixin, mixins.ListModelMixin, GenericViewSet):
    serializer_class = PermissionCRUDSerializer
    permission_classes = USER_MANAGEMENT_OPTIONS.apis["permission"]["crud"]["permission_classes"]

    def get_queryset(self):
        return Permission.objects.all()
