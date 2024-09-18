from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {"null": True, "blank": True}


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name="Email", max_length=255)

    tg_id = models.CharField(max_length=50, verbose_name="telegram_id", **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"