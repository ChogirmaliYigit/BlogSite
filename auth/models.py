from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager
from phonenumber_field.modelfields import PhoneNumberField

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(max_length=255, unique=True)
    phone_number = PhoneNumberField()
    bio = models.TextField(blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self) -> str:
        return self.email
