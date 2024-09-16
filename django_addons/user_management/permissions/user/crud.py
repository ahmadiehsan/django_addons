from rest_framework import permissions

from django_addons.user_management.utils.user_app_label import get_user_model_app_label


class CanAddUserPermission(permissions.BasePermission):
    _app_label = get_user_model_app_label()

    def has_permission(self, request, view):  # pylint: disable=unused-argument
        return request.user.has_perm(f"{self._app_label}.add_user")
