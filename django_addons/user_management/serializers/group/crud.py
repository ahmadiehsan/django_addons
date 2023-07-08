from django.contrib.auth.models import Group, Permission
from rest_framework import serializers

from django_addons.user_management.serializers.permission.minimal import PermissionMinimalSerializer


class GroupCRUDSerializer(serializers.ModelSerializer):
    permissions = PermissionMinimalSerializer(many=True, read_only=True)
    permission_ids = serializers.PrimaryKeyRelatedField(
        source='permissions', many=True, write_only=True, queryset=Permission.objects.all()
    )

    class Meta:
        model = Group
        fields = ('id', 'name', 'permissions', 'permission_ids')
