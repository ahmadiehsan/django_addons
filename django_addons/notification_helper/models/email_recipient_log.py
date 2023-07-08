from django.db import models
from django.utils.translation import gettext_lazy as _

from django_addons.django_helper.models.base import AbstractBaseModel
from django_addons.notification_helper.models import EmailLog


class EmailRecipientLog(AbstractBaseModel):
    email_log = models.ForeignKey(EmailLog, verbose_name=_('Recipient'), on_delete=models.CASCADE)
    recipient = models.EmailField(_('Recipient'))

    class Meta(AbstractBaseModel.Meta):
        verbose_name = _('Email Recipient Log')
        verbose_name_plural = _('Email Recipient Logs')
