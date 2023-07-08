from django.contrib.auth import get_user_model
from django.db import transaction

User = get_user_model()


class UserCommandRepository:
    @staticmethod
    def create(user: User, password=None):
        with transaction.atomic():
            user.save()

            if password:
                user.set_password(password)
                user.save()

        return user
