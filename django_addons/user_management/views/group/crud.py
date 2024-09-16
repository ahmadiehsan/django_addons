from django.contrib.auth.models import Group
from rest_framework.viewsets import ModelViewSet

from django_addons.user_management.options.opts import USER_MANAGEMENT_OPTIONS
from django_addons.user_management.serializers.group.crud import GroupCRUDSerializer


class GroupCRUDView(ModelViewSet):
    serializer_class = GroupCRUDSerializer
    permission_classes = USER_MANAGEMENT_OPTIONS.apis["group"]["crud"]["permission_classes"]

    def get_queryset(self):
        return Group.objects.prefetch_related("permissions").all()
