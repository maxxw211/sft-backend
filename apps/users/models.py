from django.contrib.auth.models import AbstractUser
from django.db import models

from apps.users.managers import UserManager


class User(AbstractUser):
    email = models.EmailField(max_length=128, unique=True)
    is_owner = models.BooleanField(default=False)

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self) -> str:
        return self.email
