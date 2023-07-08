from dataclasses import dataclass

from django.conf import settings
from django.core.mail import send_mail
from django.db import transaction

from django_addons.notification_helper.models import EmailLog, EmailRecipientLog


class EmailService:
    @dataclass
    class SendDTO:
        subject: str
        html_message: str
        plain_message: str
        recipient_list: list[str]

    @staticmethod
    def send(dto: SendDTO):
        with transaction.atomic():
            email_log_model = EmailLog(subject=dto.subject, html_message=dto.html_message)
            email_log_model.save()

            recipient_list = []
            for recipient in dto.recipient_list:
                recipient_list.append(EmailRecipientLog(email_log=email_log_model, recipient=recipient))

            EmailRecipientLog.objects.bulk_create(recipient_list)

        from_email = settings.DEFAULT_FROM_EMAIL
        send_mail(dto.subject, dto.plain_message, from_email, dto.recipient_list, html_message=dto.html_message)
