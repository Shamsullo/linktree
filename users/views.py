from django.core.exceptions import ValidationError
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.views import (
    PasswordChangeView, PasswordChangeDoneView,
)
from django.views.generic import (
    CreateView, TemplateView, FormView, UpdateView,
)
from .forms import (
    CustomUserCreationForm, UserPhoneNumberForm, CustomUserChangeForm,
    CustomSetPasswordForm, UserResetPasswordNumberForm
)

User = get_user_model()


class RegistrationNumberView(FormView):
    """View to get user phone number for account registration"""
    template_name = 'pages/registration-number.html'
    form_class = UserPhoneNumberForm
    success_url = reverse_lazy('registration-submit_page')

    def form_valid(self, form):
        """
        If the form is valid, save phone number in the sessions
        and redirect to the supplied URL.
        """
        self.request.session['phone_number'] = form.cleaned_data['phone_number']
        return HttpResponseRedirect(self.get_success_url())


class RegistrationSubmitView(TemplateView):
    template_name = 'pages/registration-submit.html'


class UserRegistrationsView(CreateView):
    """
    This view takes user info from user input, phone number from sessions then
    creates a new User
    """
    model = User
    success_url = reverse_lazy('home')
    form_class = CustomUserCreationForm
    template_name = 'pages/registration.html'

    def form_valid(self, form):
        user = form.save(commit=False)
        phone_number = self.request.session.get('phone_number')
        user.phone_number = phone_number
        user.save()
        return HttpResponseRedirect(self.success_url)


class EditProfileView(LoginRequiredMixin, UpdateView):
    """View to update the users personal information"""
    model = User
    form_class = CustomUserChangeForm
    context_object_name = 'data'
    template_name = 'pages/edit-profile.html'


class UserPasswordUpdate(PasswordChangeView):
    """View to show the update password fields and redirect if it is valid"""
    template_name = 'pages/change-password.html'
    success_url = reverse_lazy('password-change-done')


class UserPasswordUpdateDone(PasswordChangeDoneView):
    """Vies to display password change confirmation """
    template_name = 'pages/change-password-done.html'


class ChangeNumberView(FormView):
    """View to get the new phone number of the user"""
    template_name = 'pages/change-number.html'
    form_class = UserPhoneNumberForm
    success_url = reverse_lazy('change-num-submit_page')

    def form_valid(self, form):
        """
        If the form is valid, save phone number in the sessions
        and redirect to the supplied URL.
        """
        self.request.session['phone_number'] = form.cleaned_data['phone_number']
        return HttpResponseRedirect(self.get_success_url())


class ChangeNumberSubmitView(LoginRequiredMixin, FormView):
    """View to display code submission for changing user's phone number"""
    form_class = UserPhoneNumberForm
    template_name = 'pages/change-number-submit.html'
    success_url = reverse_lazy('password-change-done')

    def form_valid(self, form):
        user = self.request.user
        user.phone_number = self.request.session.get('phone_number')
        user.save(update_fields=['phone_number'])
        return HttpResponseRedirect(self.success_url)


class ResetPasswordNumberView(FormView):
    """View to the user phone number for restoring his/her password"""
    template_name = 'pages/password-reset-number.html'
    form_class = UserResetPasswordNumberForm
    success_url = reverse_lazy("reset-password-num-submit_page")

    def form_valid(self, form):
        self.request.session['phone_number'] = form.cleaned_data[
            'phone_number']
        return HttpResponseRedirect(self.get_success_url())


class ResetPasswordNumberSubmitView(TemplateView):
    """View for displaying code submission page for verifying phone number"""
    template_name = 'pages/password-reset-number-submit.html'


class SetNewPasswordView(FormView):
    """View for restoring user password"""
    form_class = CustomSetPasswordForm
    template_name = 'pages/password-reset.html'
    success_url = reverse_lazy('password-reset-done')

    def form_valid(self, form):
        try:
            user = User.objects.get(
                phone_number=self.request.session['phone_number'])
        except User.DoesNotExist as err:
            raise ValidationError(
                _('User with this phone number does not exist.'), err)
        user.set_password(form.cleaned_data['new_password1'])
        user.save(update_fields=['password'])
        return HttpResponseRedirect(self.get_success_url())
