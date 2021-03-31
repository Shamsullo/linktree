from django.urls import path
from .views import (
    SignUpFormView,
    already_exist,
)
from django.views.generic.base import TemplateView


urlpatterns = [
    path('signup/', SignUpFormView.as_view(), name='signup'),
    path('already_exist/', already_exist, name='checking_for_existance'),
]