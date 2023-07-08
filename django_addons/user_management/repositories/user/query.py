from django.contrib.auth import get_user_model
from django.db.models import Q

User = get_user_model()


class UserQueryRepository:
    @staticmethod
    def all():
        return User.objects.all()

    @classmethod
    def all_except_inactive_ones(cls):
        return cls.all().filter(Q(is_active=True) | Q(is_active=False, invited_by__isnull=False))

    @classmethod
    def get_by_username(cls, username):
        return cls.all().get(**{User.USERNAME_FIELD: username})

    @classmethod
    def get_by_email(cls, email):
        return cls.all().get(**{User.EMAIL_FIELD: email})

    @classmethod
    def get_by_username_or_email(cls, username_or_email):
        try:
            user = cls.get_by_username(username_or_email)
        except User.DoesNotExist:
            user = cls.get_by_email(username_or_email)

        return user
