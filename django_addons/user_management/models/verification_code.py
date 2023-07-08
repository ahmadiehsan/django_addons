from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

from django_addons.django_helper.models.base import AbstractBaseModel

User = get_user_model()


class VerificationCode(AbstractBaseModel):
    class Action(models.TextChoices):
        FORGET = 'FO', _('Forget')
        REGISTER = 'RE', _('Register')
        INVITE = 'IN', _('Invite')
        EMAIL_CHANGE = 'EM', _('Email Change')

    class IsFor(models.TextChoices):
        EMAIL = 'EM', _('Email')

    code = models.CharField(_('Code'), max_length=6)
    user = models.ForeignKey(User, verbose_name=_('User'), on_delete=models.CASCADE)
    action = models.CharField(_('Action'), max_length=2, choices=Action.choices)
    expires_at = models.DateTimeField(_('Expires At'))
    is_for = models.CharField(_('Is For'), max_length=2, choices=IsFor.choices)
    is_used = models.BooleanField(_('Is Used'), default=False)
    additional_data = models.TextField(_('Additional Data'), null=True, blank=True)

    def __str__(self):
        return self.code

    class Meta(AbstractBaseModel.Meta):
        verbose_name = _('Verification Code')
        verbose_name_plural = _('Verification Codes')
