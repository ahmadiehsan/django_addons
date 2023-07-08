from django.contrib.auth import get_user_model

User = get_user_model()


class UserChangePasswordService:
    @staticmethod
    def change_password(user: User, new_password):
        user.set_password(new_password)
        user.save()
