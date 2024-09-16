from dataclasses import dataclass
from datetime import timedelta

from django.contrib.auth import get_user_model
from django.db import transaction
from django.utils import timezone
from django.utils.translation import gettext as _

from django_addons.notification_helper.services.email_channel.email import EmailService
from django_addons.notification_helper.services.email_channel.email_template import EmailTemplateService
from django_addons.user_management.models import VerificationCode
from django_addons.user_management.repositories.user.command import UserCommandRepository
from django_addons.user_management.repositories.verification_code.command import VerificationCodeCommandRepository
from django_addons.user_management.services.user.utils import generate_random_code

User = get_user_model()


class UserRegistrationService:
    def __init__(self):
        self.user_command_repository = UserCommandRepository()
        self.verification_code_command_repository = VerificationCodeCommandRepository()
        self.email_service = EmailService()
        self.email_template_service = EmailTemplateService()

    @dataclass
    class RegisterDTO:
        username: str
        email: str
        first_name: str
        last_name: str
        password: str
        additional_fields: dict

    def register(self, dto: RegisterDTO):
        with transaction.atomic():
            user = self._create_user(dto)
            email_code = self._create_email_verification_code(user)

        self._send_email(user.email, email_code)

        return user

    @staticmethod
    def activate(user: User):
        user.is_active = True
        user.save()

    def _create_user(self, dto: RegisterDTO):
        user_model = User(
            username=dto.username,
            email=dto.email,
            first_name=dto.first_name,
            last_name=dto.last_name,
            is_active=False,
            **dto.additional_fields,
        )
        user = self.user_command_repository.create(user_model, dto.password)

        return user

    def _create_email_verification_code(self, user: User):
        verification_code_model = VerificationCode(
            code=generate_random_code(),
            user=user,
            action=VerificationCode.Action.REGISTER,
            expires_at=timezone.now() + timedelta(hours=24),
            is_for=VerificationCode.IsFor.EMAIL,
        )
        verification_code = self.verification_code_command_repository.create(verification_code_model)

        return verification_code.code

    def _send_email(self, email, code):
        subject = _("Account Verification")
        html_message, plain_message = self.email_template_service.render(
            "user_management/email_verification.html", {"verification_code": code}
        )
        self.email_service.send(self.email_service.SendDTO(subject, html_message, plain_message, [email]))
