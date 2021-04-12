from django.urls import path

from .views import SignInView, RegistrationView, RegistrationNumberView, ChangePasswordView, \
    RegistrationSubmitView, EditProfileView, ChangeNumberSubmitView, ChangeNumberView, IndexView

urlpatterns = [
    path('sign-in', SignInView.as_view(), name='sign-in_page'),
    path('edit-profile', EditProfileView.as_view(), name='edit-profile'),
    path('change-password', ChangePasswordView.as_view(), name='change-password_page'),
    path('change-number-submit', ChangeNumberSubmitView.as_view(), name='change-num-submit_page'),
    path('change-number', ChangeNumberView.as_view(), name='change-num_page'),
    path('', IndexView.as_view(), name='index_page'),
]
