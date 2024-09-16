from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

from django_addons.user_management.repositories.user.query import UserQueryRepository

User = get_user_model()


class UsernameOrEmailAuthBackend(ModelBackend):
    def authenticate(self, request, **kwargs):
        # pylint: disable=unused-argument

        user = self._get_user_object(kwargs)
        if not user:
            return None

        if not self._check_user_password(user, kwargs):
            return None

        self._raise_if_user_is_not_active(user)

        self.raise_for_custom_validation(user, request, kwargs)

        return user

    @staticmethod
    def _get_user_object(kwargs):
        username_or_email = kwargs.get(User.USERNAME_FIELD, None)

        try:
            user = UserQueryRepository.get_by_username_or_email(username_or_email)
        except User.DoesNotExist:
            user = None

        return user

    @staticmethod
    def _check_user_password(user, kwargs):
        return user.check_password(kwargs.get("password", None))

    @staticmethod
    def _raise_if_user_is_not_active(user):
        if not user.is_active:
            raise ValidationError(_("The user isn't active"))

    def raise_for_custom_validation(self, user, request, kwargs):
        pass
