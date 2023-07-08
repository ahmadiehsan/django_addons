from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError as DjangoValidationError
from django.utils.translation import gettext as _
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import SerializerMetaclass

User = get_user_model()


class PasswordSerializerMixin(metaclass=SerializerMetaclass):
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise ValidationError(_('Passwords are not equal'))

        return attrs

    @staticmethod
    def validate_password(password):
        try:
            validate_password(password)
        except DjangoValidationError as err:
            raise ValidationError(_('Unacceptable password')) from err

        return password

    class Meta:
        fields = ('password', 'confirm_password')
