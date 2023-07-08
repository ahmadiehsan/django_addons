from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.utils.translation import gettext as _
from rest_framework import serializers

User = get_user_model()


class GroupAssignmentSerializer(serializers.ModelSerializer):
    group_ids = serializers.PrimaryKeyRelatedField(
        source='groups', many=True, write_only=True, queryset=Group.objects.all()
    )

    class Meta:
        model = User
        fields = ('group_ids',)

    def to_representation(self, instance):  # pylint: disable=unused-argument
        return {'detail': _('The groups have been assigned successfully')}
