from django.contrib.admin import register
from django.utils.safestring import mark_safe

from django_addons.django_helper.admin.base import BaseAdmin
from django_addons.notification_helper.admin import EmailRecipientLogInline
from django_addons.notification_helper.models import EmailLog


@register(EmailLog)
class EmailLogAdmin(BaseAdmin):
    inlines = [EmailRecipientLogInline]
    exclude = ["html_message"]

    def get_fields(self, request, obj=None):
        return super().get_fields(request, obj) + ["html_message_parsed"]

    @staticmethod
    def html_message_parsed(obj: EmailLog):
        return mark_safe(obj.html_message)  # nosec

    def has_add_permission(self, request):
        # pylint: disable=unused-argument
        return False

    def has_change_permission(self, request, obj=None):
        # pylint: disable=unused-argument
        return False
