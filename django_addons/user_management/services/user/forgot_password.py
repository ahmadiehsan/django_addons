from datetime import timedelta

from django.contrib.auth import get_user_model
from django.utils import timezone
from django.utils.translation import gettext as _

from django_addons.notification_helper.services.email_channel.email import EmailService
from django_addons.notification_helper.services.email_channel.email_template import EmailTemplateService
from django_addons.user_management.models import VerificationCode
from django_addons.user_management.repositories.verification_code.command import VerificationCodeCommandRepository
from django_addons.user_management.services.user.utils import generate_random_code

User = get_user_model()


class UserForgotPasswordService:
    def __init__(self):
        self.verification_code_command_repository = VerificationCodeCommandRepository()
        self.email_service = EmailService()
        self.email_template_service = EmailTemplateService()

    def recover(self, user: User):
        email_code = self._create_email_verification_code(user)
        self._send_email(user.email, email_code)

    def _create_email_verification_code(self, user: User):
        verification_code_model = VerificationCode(
            code=generate_random_code(),
            user=user,
            action=VerificationCode.Action.FORGET,
            expires_at=timezone.now() + timedelta(hours=5),
            is_for=VerificationCode.IsFor.EMAIL,
        )
        verification_code = self.verification_code_command_repository.create(verification_code_model)

        return verification_code.code

    def _send_email(self, email, code):
        subject = _('Forgot Password Code')
        html_message, plain_message = self.email_template_service.render(
            'user_management/email_forgot_password.html', {'forgot_password_code': code}
        )
        self.email_service.send(self.email_service.SendDTO(subject, html_message, plain_message, [email]))
