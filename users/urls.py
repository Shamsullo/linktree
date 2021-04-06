from django.contrib.auth.views import LoginView, PasswordChangeView, \
    PasswordChangeDoneView
from django.urls import path
from django.views.generic import TemplateView

from .views import (
    SignUpFormView, ProfileViewClass, UserPasswordUpdate, update_first_name,
    update_last_name, already_exist, UpdatePhoneNumberView,
)


urlpatterns = [
    path('signup/', SignUpFormView.as_view(), name='signup'),
    path('already-exist/', already_exist, name='check_for_existence'),
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('profile/<int:pk>/', ProfileViewClass.as_view(), name='profile'),
    path('first-name-update/', update_first_name, name='first_name_update'),
    path('last-name-update/', update_last_name, name='last_name_update'),
    path('pasword-change/', UserPasswordUpdate.as_view(), name='password-change'),
    path('password-change-done/', PasswordChangeDoneView.as_view(
        template_name='users/password_update_done.html'),
         name='password-change-done'),
    path('phone-number-change-done/', TemplateView.as_view(
        template_name='users/phone_number_change_done.html'),
         name='phone-number-change-done'),
    # path('phone-number_change-abc/<int:pk>/', UpdatePhoneNumberViewAbc.as_view(),
    #      name='phone-number-change-abc'),
    path('phone-number-change/', UpdatePhoneNumberView.as_view(),
         name='phone-number-change'),
]
