from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from django_addons.user_management.models import VerificationCode
from django_addons.user_management.options.opts import USER_MANAGEMENT_OPTIONS
from django_addons.user_management.serializers.verification_code.crud import VerificationCodeCRUDSerializer


class VerificationCodeCRUDView(mixins.RetrieveModelMixin, mixins.ListModelMixin, GenericViewSet):
    serializer_class = VerificationCodeCRUDSerializer
    permission_classes = USER_MANAGEMENT_OPTIONS.apis["verification_code"]["crud"]["permission_classes"]

    def get_queryset(self):
        return VerificationCode.objects.all()
