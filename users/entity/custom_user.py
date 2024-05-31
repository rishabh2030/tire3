from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from rest_framework_simplejwt.tokens import RefreshToken
from django.db import models
from helper.models import BaseModel
from .user_manager import UserManager

class CustomUser(AbstractBaseUser,PermissionsMixin,BaseModel):
    USER_TYPE_CHOICES = (
        (1,'Normal User'),
        (2,'Business User'),
        (3,'Shop User'),
    )

    username = models.CharField(max_length=255, unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    phone_number = models.CharField(max_length=15, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, default=1)
    business_name = models.CharField(max_length=255, blank=True, null=True)
    shop_name = models.CharField(max_length=255, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'phone_number']

    def get_tokens(self):
        """Returns a tuple of JWT tokens (token, refresh_token)"""
        refresh = RefreshToken.for_user(self)
        return str(refresh.access_token), str(refresh)
    
    def __str__(self):
        return self.username

    def migrate_to_business_user(self, business_name):
        self.user_type = 2
        self.business_name = business_name
        self.save()

    def migrate_to_shop_owner(self, shop_name):
        self.user_type = 3
        self.shop_name = shop_name
        self.save()
