from django.contrib.auth import get_user_model
from django.utils.translation import gettext as _
from rest_framework import serializers

from django_addons.user_management.serializers.user.utils.current_password_mixin import CurrentPasswordSerializerMixin
from django_addons.user_management.services.user.change_email import UserChangeEmailService

User = get_user_model()


class UserChangeEmailSerializer(CurrentPasswordSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email',) + CurrentPasswordSerializerMixin.Meta.fields

    def create(self, validated_data):
        user = self.context['request'].user
        UserChangeEmailService().request_for_email_change(user, validated_data['email'])

        return user

    def update(self, instance, validated_data):
        raise NotImplementedError()

    def to_representation(self, instance):  # pylint: disable=unused-argument
        return {'detail': _('Confirmation email sent')}
