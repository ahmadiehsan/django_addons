from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet

from django_addons.django_helper.drf.mixins.ok_model import OKModelMixin
from django_addons.user_management.serializers.user.forgot_password_verify import UserForgotPasswordVerifySerializer


class UserForgotPasswordVerifyView(OKModelMixin, GenericViewSet):
    serializer_class = UserForgotPasswordVerifySerializer
    permission_classes = (AllowAny,)
