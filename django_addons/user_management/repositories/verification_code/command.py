import json
import logging

from django.contrib.auth import get_user_model

from django_addons.user_management.models import VerificationCode

User = get_user_model()


class VerificationCodeCommandRepository:
    @staticmethod
    def create(verification_code: VerificationCode):
        if verification_code.additional_data:
            verification_code.additional_data = json.dumps(verification_code.additional_data)

        verification_code.save()
        logging.info('A verification code was generated: %s', verification_code)

        return verification_code

    @staticmethod
    def use(verification_code: VerificationCode):
        verification_code.is_used = True
        verification_code.save()
