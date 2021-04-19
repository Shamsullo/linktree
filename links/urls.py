from django.urls import path
from .views import SocialMediaView, LinksBoardUpdateViw

urlpatterns = [
    path('social-links/', SocialMediaView.as_view(), name='add-social-links'),
    path('board/<int:pk>/', LinksBoardUpdateViw.as_view(),
         name='add-or-update-board-data')
]
