from django.urls import path
from .services.normal_user_register_view import NormalUserRegisterView

urlpatterns = [
    path('register/', NormalUserRegisterView.as_view(), name='register'),
]