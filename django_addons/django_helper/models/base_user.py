from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from django_addons.django_helper.models.id_only import AbstractIDOnlyModel


class AbstractExtendedBaseUser(AbstractUser, AbstractIDOnlyModel):
    email = models.EmailField(_('Email Address'), unique=True)
    invited_by = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.username

    class Meta(AbstractUser.Meta, AbstractIDOnlyModel.Meta):
        indexes = [models.Index(fields=['username'])]
        abstract = True
