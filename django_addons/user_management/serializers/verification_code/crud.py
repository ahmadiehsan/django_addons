from rest_framework import serializers

from django_addons.user_management.models import VerificationCode
from django_addons.user_management.serializers.user.minimal import UserMinimalSerializer


class VerificationCodeCRUDSerializer(serializers.ModelSerializer):
    user = UserMinimalSerializer(read_only=True)
    action_translated = serializers.CharField(source="get_action_display", read_only=True)
    is_for_translated = serializers.CharField(source="get_is_for_display", read_only=True)

    class Meta:
        model = VerificationCode
        fields = (
            "id",
            "code",
            "user",
            "action",
            "action_translated",
            "expires_at",
            "is_for",
            "is_for_translated",
            "is_used",
        )
