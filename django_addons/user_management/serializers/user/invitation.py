from django.contrib.auth import get_user_model
from django.utils.translation import gettext as _
from rest_framework import serializers

from django_addons.user_management.services.user.invitation import UserInvitationService

User = get_user_model()


class UserInvitationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "email")

    def create(self, validated_data):
        user = UserInvitationService().invite(validated_data["email"], self.context["request"].user)

        return user

    def update(self, instance, validated_data):
        raise NotImplementedError

    def to_representation(self, instance):  # pylint: disable=unused-argument
        return {
            "detail": _("The account has been created successfully and an invitation email has been sent to the email")
        }
