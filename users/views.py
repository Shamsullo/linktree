import json
from django.contrib.auth.views import PasswordChangeView, LoginView
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView, DetailView, TemplateView, FormView,
)
from django.contrib.auth import get_user_model
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from .forms import CustomUserCreationForm, UserPhoneNumberForm

User = get_user_model()


class SignUpFormView(CreateView):
    """
    This view takes data from request and creates a new User
    """
    model = User
    success_url = '/'
    form_class = CustomUserCreationForm
    template_name = 'users/sign_up.html'

    def form_valid(self, form):
        user = form.save(commit=False)
        phone = self.request.session.get('phone_number')
        user.phone_number = phone
        user.save()
        return HttpResponseRedirect('/')


def already_exist(request):
    if request.is_ajax and request.method == "GET":
        phone_number = request.GET.get('phoneNumber').strip('\u200e')
        data = {
            'is_taken': User.objects.filter(phone_number=phone_number).exists()
        }
        if not data['is_taken']:
            request.session['phone_number'] = phone_number

        return JsonResponse(data)


class ProfileViewClass(DetailView):
    """ Viewing User Information """
    model = User
    template_name = 'users/profile.html'
    context_object_name = 'user'


def update_first_name(request):
    if request.method == "PUT":
        try:
            data = json.load(request)
            user = User.objects.get(pk=request.user.pk)
            user.first_name = data['first_name']
            user.save()
        except User.DoesNotExist:
            return 'User with this ID does not exist!'

        return JsonResponse({'response': 'First name has been update'}, status=200)


def update_last_name(request):
    if request.method == "PUT":
        try:
            data = json.load(request)
            user = User.objects.get(pk=request.user.pk)
            user.last_name = data['last_name']
            user.save()
        except User.DoesNotExist:
            return 'User with this ID does not exist!'

        return JsonResponse({'response': 'Last name has been update'}, status=200)


class UserPasswordUpdate(PasswordChangeView):
    template_name = 'users/password_update.html'
    success_url = reverse_lazy('password-change-done')


class UpdatePhoneNumberView(CreateView):
    model = User
    success_url = reverse_lazy('home')
    fields = ('phone_number',)
    template_name = 'users/phone_number_change.html'

    def post(self, request, *args, **kwargs):
        new_phone_number = json.load(request)['phone_number']
        user = User.objects.get(pk=request.user.pk)
        user.phone_number = new_phone_number
        user.save()
        return HttpResponseRedirect('/')


class SigInView(LoginView):
    template_name = 'pages/sign-in.html'


class RegistrationNumberView(FormView):
    template_name = 'pages/registration-number.html'
    form_class = UserPhoneNumberForm
    success_url = reverse_lazy('registration-submit_page')


class RegistrationSubmitView(TemplateView):
    template_name = 'pages/registration-submit.html'
