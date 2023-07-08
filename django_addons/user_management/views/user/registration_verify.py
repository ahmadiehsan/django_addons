from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet

from django_addons.django_helper.drf.mixins.ok_model import OKModelMixin
from django_addons.user_management.serializers.user.registration_verify import UserRegistrationVerifySerializer


class UserRegistrationVerifyView(OKModelMixin, GenericViewSet):
    serializer_class = UserRegistrationVerifySerializer
    permission_classes = (AllowAny,)
