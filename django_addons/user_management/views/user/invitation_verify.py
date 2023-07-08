from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet

from django_addons.django_helper.drf.mixins.ok_model import OKModelMixin
from django_addons.user_management.serializers.user.invitation_verify import UserInvitationVerifySerializer


class UserInvitationVerifyView(OKModelMixin, GenericViewSet):
    serializer_class = UserInvitationVerifySerializer
    permission_classes = (AllowAny,)
