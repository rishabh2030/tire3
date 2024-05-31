from django.urls import path
from .services.normal_user_register_view import NormalUserRegisterView
from .services.login_api_view import UserLoginView

urlpatterns = [
    path('register/', NormalUserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
]