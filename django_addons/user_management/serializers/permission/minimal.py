from django.contrib.auth.models import Permission
from rest_framework import serializers


class PermissionMinimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = ('id', 'name', 'codename')
        read_only = True
