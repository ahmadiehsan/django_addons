import json

from django.db import transaction
from django.utils.translation import gettext as _
from rest_framework import serializers

from django_addons.user_management.models import VerificationCode
from django_addons.user_management.repositories.verification_code.command import VerificationCodeCommandRepository
from django_addons.user_management.repositories.verification_code.query import VerificationCodeQueryRepository
from django_addons.user_management.services.user.change_email import UserChangeEmailService


class UserChangeEmailVerifySerializer(serializers.Serializer):
    code = serializers.SlugRelatedField(
        source="verification_code",
        write_only=True,
        queryset=VerificationCodeQueryRepository.get_all_not_expired(VerificationCode.Action.EMAIL_CHANGE),
        slug_field="code",
    )

    class Meta:
        fields = ("code",)

    def create(self, validated_data):
        verification_code = validated_data["verification_code"]

        with transaction.atomic():
            VerificationCodeCommandRepository.use(verification_code)
            new_email = json.loads(verification_code.additional_data)["new_email"]
            UserChangeEmailService().do_change(verification_code.user, new_email)

        return verification_code

    def update(self, instance, validated_data):
        raise NotImplementedError

    def to_representation(self, instance):  # pylint: disable=unused-argument
        return {"detail": _("The email has been changed successfully")}
