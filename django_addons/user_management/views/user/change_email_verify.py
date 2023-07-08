from rest_framework.viewsets import GenericViewSet

from django_addons.django_helper.drf.mixins.ok_model import OKModelMixin
from django_addons.user_management.options.opts import USER_MANAGEMENT_OPTIONS
from django_addons.user_management.serializers.user.change_email_verify import UserChangeEmailVerifySerializer


class UserChangeEmailVerifyView(OKModelMixin, GenericViewSet):
    serializer_class = UserChangeEmailVerifySerializer
    permission_classes = USER_MANAGEMENT_OPTIONS.apis['user']['change_email']['permission_classes']
