from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.utils.translation import gettext as _
from rest_framework import serializers

User = get_user_model()


class PermissionAssignmentSerializer(serializers.ModelSerializer):
    permission_ids = serializers.PrimaryKeyRelatedField(
        source="user_permissions", many=True, write_only=True, queryset=Permission.objects.all()
    )

    class Meta:
        model = User
        fields = ("permission_ids",)

    def to_representation(self, instance):  # pylint: disable=unused-argument
        return {"detail": _("The permissions have been assigned successfully")}
