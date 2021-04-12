from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where phone number is the unique identifiers
    for authentication instead of usernames.
    """

    def create_user(self, phone_number, password, **extra_fields):
        """
        Create and save a User with the given phone number and password.
        """
        if not phone_number:
            raise ValueError(_('The phone_number must be set'))
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, phone_number, password):
        """
        Create and save a SuperUser with the given phone_number and password.
        """
        user = self.create_user(
            phone_number,
            password=password,
        )
        user.is_active = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user
