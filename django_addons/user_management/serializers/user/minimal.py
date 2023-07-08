from django.contrib.auth import get_user_model
from rest_framework import serializers

from django_addons.user_management.options.opts import USER_MANAGEMENT_OPTIONS

User = get_user_model()


class UserMinimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name') + USER_MANAGEMENT_OPTIONS.additional_fields[
            'user'
        ]
        read_only = True
