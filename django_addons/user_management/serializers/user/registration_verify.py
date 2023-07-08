from django.db import transaction
from django.utils.translation import gettext as _
from rest_framework import serializers

from django_addons.user_management.models import VerificationCode
from django_addons.user_management.repositories.verification_code.command import VerificationCodeCommandRepository
from django_addons.user_management.repositories.verification_code.query import VerificationCodeQueryRepository
from django_addons.user_management.services.user.registration import UserRegistrationService


class UserRegistrationVerifySerializer(serializers.Serializer):
    code = serializers.SlugRelatedField(
        source='verification_code',
        write_only=True,
        queryset=VerificationCodeQueryRepository.get_all_not_expired(VerificationCode.Action.REGISTER),
        slug_field='code',
    )

    class Meta:
        fields = ('code',)

    def create(self, validated_data):
        verification_code = validated_data['verification_code']

        with transaction.atomic():
            VerificationCodeCommandRepository.use(verification_code)
            UserRegistrationService().activate(verification_code.user)

        return verification_code

    def update(self, instance, validated_data):
        raise NotImplementedError()

    def to_representation(self, instance):  # pylint: disable=unused-argument
        return {'detail': _('The account has been activated successfully')}
