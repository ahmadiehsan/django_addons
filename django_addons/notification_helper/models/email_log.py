from django.db import models
from django.utils.translation import gettext_lazy as _

from django_addons.django_helper.models.base import AbstractBaseModel


class EmailLog(AbstractBaseModel):
    subject = models.CharField(_('Subject'), max_length=255)
    html_message = models.TextField(_('HTML Message'))

    def __str__(self):
        return self.subject

    class Meta(AbstractBaseModel.Meta):
        verbose_name = _('Email Log')
        verbose_name_plural = _('Email Logs')
