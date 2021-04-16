from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path
from django.views.generic import TemplateView
from .views import (
    UserPasswordUpdate, RegistrationNumberView, RegistrationSubmitView,
    UserRegistrationsView, EditProfileView, UserPasswordUpdateDone,
    ChangeNumberView, ChangeNumberSubmitView, SetNewPasswordView,
    ResetPasswordNumberView, ResetPasswordNumberSubmitView,
)

urlpatterns = [
    path('registration-number/', RegistrationNumberView.as_view(),
         name='reg-number_page'),
    path('registration-submit/', RegistrationSubmitView.as_view(),
         name='registration-submit_page'),
    path('registration/', UserRegistrationsView.as_view(), name='reg_page'),
    path('login/', LoginView.as_view(template_name='pages/sign-in.html'),
         name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('edit-profile/<int:pk>/', EditProfileView.as_view(),
         name='edit-profile'),
    path('pasword-change/', UserPasswordUpdate.as_view(),
         name='password-change'),
    path('password-change-done/', UserPasswordUpdateDone.as_view(),
         name='password-change-done'),
    path('change-number/', ChangeNumberView.as_view(), name='change-num_page'),
    path('change-number-submit/', ChangeNumberSubmitView.as_view(),
         name='change-num-submit_page'),
    path('reseet-password-number/', ResetPasswordNumberView.as_view(),
         name='reset-password-num_page'),
    path('reset-password-number-submit/', ResetPasswordNumberSubmitView.as_view(),
         name='reset-password-num-submit_page'),
    path('reset-password/', SetNewPasswordView.as_view(),
         name='reset-password_page'),
    path('reset-password-done/', TemplateView.as_view(
        template_name='pages/password-reset-done.html'),
         name='password-reset-done')
]
