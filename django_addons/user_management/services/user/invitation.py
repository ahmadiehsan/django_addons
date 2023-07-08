from dataclasses import dataclass
from datetime import timedelta
from uuid import uuid4

from django.contrib.auth import get_user_model
from django.db import transaction
from django.utils import timezone
from django.utils.translation import gettext as _

from django_addons.notification_helper.services.email_channel.email import EmailService
from django_addons.notification_helper.services.email_channel.email_template import EmailTemplateService
from django_addons.user_management.models import VerificationCode
from django_addons.user_management.options.opts import USER_MANAGEMENT_OPTIONS
from django_addons.user_management.repositories.user.command import UserCommandRepository
from django_addons.user_management.repositories.verification_code.command import VerificationCodeCommandRepository
from django_addons.user_management.services.user.change_password import UserChangePasswordService
from django_addons.user_management.services.user.utils import generate_random_code

User = get_user_model()


class UserInvitationService:
    def __init__(self):
        self.user_command_repository = UserCommandRepository()
        self.user_change_password_service = UserChangePasswordService()
        self.verification_code_command_repository = VerificationCodeCommandRepository()
        self.email_service = EmailService()
        self.email_template_service = EmailTemplateService()

    @dataclass
    class AcceptDTO:
        user: User
        username: str
        first_name: str
        last_name: str
        password: str
        additional_fields: dict

    def invite(self, email, invited_by: User):
        with transaction.atomic():
            user_model = User(username=str(uuid4()), email=email, invited_by=invited_by, is_active=False)
            user = self.user_command_repository.create(user_model)
            email_code = self._create_email_invitation_code(user)

        self._send_email(user.email, email_code)

        return user

    def accept(self, dto: AcceptDTO):
        user = dto.user

        with transaction.atomic():
            self._add_user_data(user, dto)
            self.user_change_password_service.change_password(user, dto.password)

    @staticmethod
    def _add_user_data(user: User, dto: AcceptDTO):
        user.username = dto.username
        user.first_name = dto.first_name
        user.last_name = dto.last_name
        user.is_active = True

        for field, field_value in dto.additional_fields.items():
            setattr(user, field, field_value)

        user.save()

    def _create_email_invitation_code(self, user: User):
        verification_code_model = VerificationCode(
            code=generate_random_code(),
            user=user,
            action=VerificationCode.Action.INVITE,
            expires_at=timezone.now() + timedelta(days=5),
            is_for=VerificationCode.IsFor.EMAIL,
        )
        verification_code = self.verification_code_command_repository.create(verification_code_model)

        return verification_code.code

    def _send_email(self, email, code):
        subject = _('Invitation')
        html_message, plain_message = self.email_template_service.render(
            'user_management/email_invitation.html',
            {
                'invitation_code': code,
                'invitation_link': USER_MANAGEMENT_OPTIONS.email_data['invitation_acceptance_link'],
            },
        )
        self.email_service.send(self.email_service.SendDTO(subject, html_message, plain_message, [email]))
