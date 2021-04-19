from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.shortcuts import reverse
from django.utils.translation import ugettext_lazy as _

from .managers import CustomUserManager


class CustomUser(PermissionsMixin, AbstractBaseUser):
    """Customized user model for our project"""
    phone_number = models.CharField(_('phone number'), max_length=30, unique=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    birthdate = models.DateField(_('birthdate'), null=True, blank=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_(
            'Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return self.phone_number

    def get_username(self):
        return self.phone_number

    def get_absolute_url(self):
        return reverse("edit-profile", kwargs={"pk": self.pk})
