from time import sleep

from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser
from django.utils.translation import gettext as _
from rest_framework import serializers

from django_addons.user_management.repositories.user.query import UserQueryRepository
from django_addons.user_management.services.user.forgot_password import UserForgotPasswordService

User = get_user_model()


class UserForgotPasswordSerializer(serializers.Serializer):
    identifier = serializers.CharField(source='user', write_only=True, help_text=_('Username or Email'))

    @staticmethod
    def validate_identifier(value):
        try:
            user = UserQueryRepository.get_by_username_or_email(value)
        except User.DoesNotExist:
            user = AnonymousUser()  # For security reasons we shouldn't raise an error here

        return user

    class Meta:
        fields = ('identifier',)

    def create(self, validated_data):
        user = validated_data['user']

        if not user.is_anonymous:
            UserForgotPasswordService().recover(user)
        else:
            sleep(4)  # For security reasons, we should simulate an email-sending scenario

        return user

    def update(self, instance, validated_data):
        raise NotImplementedError()

    def to_representation(self, instance):  # pylint: disable=unused-argument
        return {'detail': _('If the username or email is in the system, you will receive a password reset email.')}
