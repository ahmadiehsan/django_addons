from django.contrib.auth import get_user_model
from django.db import transaction
from django.utils.translation import gettext as _
from rest_framework import serializers

from django_addons.user_management.models import VerificationCode
from django_addons.user_management.repositories.verification_code.command import VerificationCodeCommandRepository
from django_addons.user_management.repositories.verification_code.query import VerificationCodeQueryRepository
from django_addons.user_management.serializers.user.utils.password_mixin import PasswordSerializerMixin
from django_addons.user_management.services.user.change_password import UserChangePasswordService

User = get_user_model()


class UserForgotPasswordVerifySerializer(PasswordSerializerMixin, serializers.Serializer):
    code = serializers.SlugRelatedField(
        source="verification_code",
        write_only=True,
        queryset=VerificationCodeQueryRepository.get_all_not_expired(VerificationCode.Action.FORGET),
        slug_field="code",
    )

    class Meta:
        fields = ("code",) + PasswordSerializerMixin.Meta.fields

    def create(self, validated_data):
        verification_code = validated_data["verification_code"]

        with transaction.atomic():
            VerificationCodeCommandRepository.use(verification_code)
            UserChangePasswordService().change_password(verification_code.user, validated_data["password"])

        return verification_code

    def update(self, instance, validated_data):
        raise NotImplementedError

    def to_representation(self, instance):  # pylint: disable=unused-argument
        return {"detail": _("The password has been updated successfully")}
