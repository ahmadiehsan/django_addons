from django.contrib.auth import get_user_model
from django.db import transaction
from django.utils.translation import gettext as _
from rest_framework import serializers

from django_addons.user_management.models import VerificationCode
from django_addons.user_management.options.opts import USER_MANAGEMENT_OPTIONS
from django_addons.user_management.repositories.verification_code.command import VerificationCodeCommandRepository
from django_addons.user_management.repositories.verification_code.query import VerificationCodeQueryRepository
from django_addons.user_management.serializers.user.utils.password_mixin import PasswordSerializerMixin
from django_addons.user_management.services.user.invitation import UserInvitationService

User = get_user_model()


class UserInvitationVerifySerializer(PasswordSerializerMixin, serializers.ModelSerializer):
    code = serializers.SlugRelatedField(
        source='verification_code',
        write_only=True,
        queryset=VerificationCodeQueryRepository.get_all_not_expired(VerificationCode.Action.INVITE),
        slug_field='code',
    )

    class Meta:
        model = User
        fields = (
            ('id', 'username', 'first_name', 'last_name', 'code')
            + PasswordSerializerMixin.Meta.fields
            + USER_MANAGEMENT_OPTIONS.additional_fields['user']
        )

    def create(self, validated_data):
        verification_code = validated_data['verification_code']

        with transaction.atomic():
            VerificationCodeCommandRepository.use(verification_code)
            UserInvitationService().accept(
                UserInvitationService.AcceptDTO(
                    verification_code.user,
                    validated_data['username'],
                    validated_data.get('first_name', ''),
                    validated_data.get('last_name', ''),
                    validated_data['password'],
                    {field: validated_data.get(field) for field in USER_MANAGEMENT_OPTIONS.additional_fields['user']},
                )
            )

        return verification_code

    def update(self, instance, validated_data):
        raise NotImplementedError()

    def to_representation(self, instance):  # pylint: disable=unused-argument
        return {'detail': _('The account was updated and activated successfully')}
