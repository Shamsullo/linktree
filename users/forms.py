from django import forms
from django.contrib.auth import get_user_model, password_validation
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.forms import (
    UserCreationForm, UserChangeForm,
)
from .models import CustomUser

User = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    """Form for creating a new user to the system"""

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('first_name', 'last_name', 'birthdate',
                  'password1', 'password2')


class CustomUserChangeForm(UserChangeForm):
    """Form for changing the user name and surname"""

    class Meta:
        model = User
        fields = ('first_name', 'last_name',)


class UserPhoneNumberForm(forms.ModelForm):
    """Form for validating is the user is exist with given phone number"""

    class Meta:
        model = User
        fields = ('phone_number',)


class UserResetPasswordNumberForm(forms.Form):
    """
    For for validating if user can restore his/her password with given phone
    number
    """
    phone_number = forms.CharField(max_length=20)

    error_messages = {
        'user_does_not_exist': _("User with is number does not exist."),
    }

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if not User.objects.filter(phone_number=phone_number).exists():
            raise forms.ValidationError(
                self.error_messages['user_does_not_exist'],
                code='user_does_not_exist',
            )
        return phone_number


class CustomSetPasswordForm(forms.Form):
    """
    A form that lets a user reset their password without entering the old
    password
    """
    error_messages = {
        'password_mismatch': _("The two password fields didn't match."),
    }
    new_password1 = forms.CharField(
        widget=forms.PasswordInput,
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        strip=False,
        widget=forms.PasswordInput,
    )

    def clean_new_password2(self):
        password1 = self.cleaned_data.get('new_password1')
        password2 = self.cleaned_data.get('new_password2')
        if password1 and password2:
            if password1 != password2:
                raise forms.ValidationError(
                    self.error_messages['password_mismatch'],
                    code='password_mismatch',
                )
        password_validation.validate_password(password2)
        return password2
