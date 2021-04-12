from django import forms
from django.contrib.auth.forms import (
    UserCreationForm, UserChangeForm,
)

from django.contrib.auth import get_user_model
from .models import CustomUser

User = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation',
                                widget=forms.PasswordInput)

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('first_name', 'last_name', 'birthdate', 'password1', 'password2')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('phone_number',)


class UserPhoneNumberForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('phone_number',)

