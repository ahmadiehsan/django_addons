from django.contrib.auth import get_user_model
from django.utils import timezone

from django_addons.user_management.models import VerificationCode

User = get_user_model()


class VerificationCodeQueryRepository:
    @staticmethod
    def get_all_not_expired(action=None):
        verification_codes = VerificationCode.objects.filter(is_used=False, expires_at__gte=timezone.now())

        if action:
            verification_codes = verification_codes.filter(action=action)

        return verification_codes
