from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(blank=True, null=True)
    nickname = models.CharField(max_length=25, blank=True)