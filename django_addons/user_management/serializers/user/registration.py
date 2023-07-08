from django.contrib.auth import get_user_model
from django.utils.translation import gettext as _
from rest_framework import serializers

from django_addons.user_management.options.opts import USER_MANAGEMENT_OPTIONS
from django_addons.user_management.serializers.user.utils.password_mixin import PasswordSerializerMixin
from django_addons.user_management.services.user.registration import UserRegistrationService

User = get_user_model()


class UserRegistrationSerializer(PasswordSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            ('id', 'username', 'email', 'first_name', 'last_name')
            + PasswordSerializerMixin.Meta.fields
            + USER_MANAGEMENT_OPTIONS.additional_fields['user']
        )

    def create(self, validated_data):
        user = UserRegistrationService().register(
            UserRegistrationService.RegisterDTO(
                validated_data['username'],
                validated_data['email'],
                validated_data.get('first_name', ''),
                validated_data.get('last_name', ''),
                validated_data['password'],
                {field: validated_data.get(field) for field in USER_MANAGEMENT_OPTIONS.additional_fields['user']},
            )
        )

        return user

    def update(self, instance, validated_data):
        raise NotImplementedError()

    def to_representation(self, instance):  # pylint: disable=unused-argument
        return {
            'detail': _('The account has been created successfully and a verification email has been sent to the email')
        }
