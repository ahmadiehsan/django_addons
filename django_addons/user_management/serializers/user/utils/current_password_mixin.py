from django.contrib.auth import get_user_model
from django.utils.translation import gettext as _
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import SerializerMetaclass

User = get_user_model()


class CurrentPasswordSerializerMixin(metaclass=SerializerMetaclass):
    current_password = serializers.CharField(write_only=True)

    def validate_current_password(self, password):
        user = self.context['request'].user

        if not user.check_password(password):
            raise ValidationError(_('Invalid password'))

        return password

    class Meta:
        fields = ('current_password',)
