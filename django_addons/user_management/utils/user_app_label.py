from django.conf import settings


def get_user_model_app_label():
    return settings.AUTH_USER_MODEL.split(".")[0]
