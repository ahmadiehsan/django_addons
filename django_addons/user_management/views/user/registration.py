from rest_framework import mixins
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet

from django_addons.user_management.serializers.user.registration import UserRegistrationSerializer


class UserRegistrationView(mixins.CreateModelMixin, GenericViewSet):
    serializer_class = UserRegistrationSerializer
    permission_classes = (AllowAny,)
