from django.contrib.admin import register

from django_addons.django_helper.admin.base import BaseAdmin
from django_addons.user_management.models import VerificationCode


@register(VerificationCode)
class VerificationCodeAdmin(BaseAdmin):
    list_display = BaseAdmin.list_display + ('is_used', 'is_for', 'action', 'expires_at')
    list_filter = BaseAdmin.list_filter + ('is_used', 'is_for', 'action')

    def has_add_permission(self, request):
        # pylint: disable=unused-argument
        return False

    def has_change_permission(self, request, obj=None):
        # pylint: disable=unused-argument
        return False
