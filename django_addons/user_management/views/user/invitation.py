from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from django_addons.user_management.options.opts import USER_MANAGEMENT_OPTIONS
from django_addons.user_management.serializers.user.invitation import UserInvitationSerializer


class UserInvitationView(mixins.CreateModelMixin, GenericViewSet):
    serializer_class = UserInvitationSerializer
    permission_classes = USER_MANAGEMENT_OPTIONS.apis["user"]["invitation"]["permission_classes"]
