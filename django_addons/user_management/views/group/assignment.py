from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from django_addons.user_management.options.opts import USER_MANAGEMENT_OPTIONS
from django_addons.user_management.repositories.user.query import UserQueryRepository
from django_addons.user_management.serializers.group.assignment import GroupAssignmentSerializer


class GroupAssignmentView(mixins.UpdateModelMixin, GenericViewSet):
    serializer_class = GroupAssignmentSerializer
    permission_classes = USER_MANAGEMENT_OPTIONS.apis["group"]["assignment"]["permission_classes"]

    def get_queryset(self):
        return UserQueryRepository.all_except_inactive_ones()
