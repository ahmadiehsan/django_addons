from django.contrib import admin

from django_addons.notification_helper.models import EmailRecipientLog


class EmailRecipientLogInline(admin.TabularInline):
    model = EmailRecipientLog
