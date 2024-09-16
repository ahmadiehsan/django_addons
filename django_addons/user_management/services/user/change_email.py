from datetime import timedelta

from django.contrib.auth import get_user_model
from django.db import transaction
from django.utils import timezone
from django.utils.translation import gettext as _

from django_addons.notification_helper.services.email_channel.email import EmailService
from django_addons.notification_helper.services.email_channel.email_template import EmailTemplateService
from django_addons.user_management.models import VerificationCode
from django_addons.user_management.repositories.verification_code.command import VerificationCodeCommandRepository
from django_addons.user_management.services.user.utils import generate_random_code

User = get_user_model()


class UserChangeEmailService:
    def __init__(self):
        self.verification_code_command_repository = VerificationCodeCommandRepository()
        self.email_service = EmailService()
        self.email_template_service = EmailTemplateService()

    def request_for_email_change(self, user: User, new_email):
        with transaction.atomic():
            email_code = self._create_email_verification_code(user, new_email)

        self._send_email(new_email, email_code)

    @staticmethod
    def do_change(user: User, new_email):
        user.email = new_email
        user.save()

    def _create_email_verification_code(self, user: User, new_email):
        verification_code_model = VerificationCode(
            code=generate_random_code(),
            user=user,
            action=VerificationCode.Action.EMAIL_CHANGE,
            expires_at=timezone.now() + timedelta(days=1),
            is_for=VerificationCode.IsFor.EMAIL,
            additional_data={"new_email": new_email},
        )
        verification_code = self.verification_code_command_repository.create(verification_code_model)

        return verification_code.code

    def _send_email(self, email, code):
        subject = _("Email Verification")
        html_message, plain_message = self.email_template_service.render(
            "user_management/email_change_email.html", {"verification_code": code}
        )
        self.email_service.send(self.email_service.SendDTO(subject, html_message, plain_message, [email]))
