from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext as _

from django_addons.user_management.options.opts import USER_MANAGEMENT_OPTIONS


class ExtendedBaseUserAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("is_active",)
    fieldsets = UserAdmin.fieldsets + (
        (_("Additional data"), {"fields": ("invited_by",) + USER_MANAGEMENT_OPTIONS.additional_fields["user"]}),
    )
    raw_id_fields = ("invited_by",)
    readonly_fields = ("invited_by",)
    add_fieldsets = ((None, {"classes": ("wide",), "fields": ("username", "email", "password1", "password2")}),)
