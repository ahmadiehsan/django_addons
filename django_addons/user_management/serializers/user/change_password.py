from django.contrib.auth import get_user_model
from django.utils.translation import gettext as _
from rest_framework import serializers

from django_addons.user_management.serializers.user.utils.current_password_mixin import CurrentPasswordSerializerMixin
from django_addons.user_management.serializers.user.utils.password_mixin import PasswordSerializerMixin
from django_addons.user_management.services.user.change_password import UserChangePasswordService

User = get_user_model()


class UserChangePasswordSerializer(
    CurrentPasswordSerializerMixin, PasswordSerializerMixin, serializers.ModelSerializer
):
    class Meta:
        model = User
        fields = CurrentPasswordSerializerMixin.Meta.fields + PasswordSerializerMixin.Meta.fields

    def create(self, validated_data):
        user = self.context['request'].user
        UserChangePasswordService().change_password(user, validated_data['password'])

        return user

    def update(self, instance, validated_data):
        raise NotImplementedError()

    def to_representation(self, instance):  # pylint: disable=unused-argument
        return {'detail': _('The password has been changed successfully')}
