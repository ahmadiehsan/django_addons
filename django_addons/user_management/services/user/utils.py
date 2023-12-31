from django.utils.crypto import get_random_string


def generate_random_code(length=6):
    return get_random_string(length=length, allowed_chars='0123456789')
