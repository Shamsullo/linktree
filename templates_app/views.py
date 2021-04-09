from django.views.generic import TemplateView


class SignInView(TemplateView):
    template_name = 'pages/sign-in.html'


class RegistrationView(TemplateView):
    template_name = 'pages/registration.html'


class RegistrationNumberView(TemplateView):
    template_name = 'pages/registration-number.html'


class RegistrationSubmitView(TemplateView):
    template_name = 'pages/registration-submit.html'


class EditProfileView(TemplateView):
    template_name = 'pages/edit-profile.html'


class ChangePasswordView(TemplateView):
    template_name = 'pages/change-password.html'


class ChangeNumberSubmitView(TemplateView):
    template_name = 'pages/change-number-submit.html'


class ChangeNumberView(TemplateView):
    template_name = 'pages/change-number.html'


class IndexView(TemplateView):
    template_name = 'pages/index.html'
