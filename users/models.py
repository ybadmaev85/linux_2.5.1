from django.contrib.auth.models import AbstractUser
from django.db import models
NULLABLE = {'blank': True, 'null': True}


class UserRole(models.TextChoices):
    MODERATOR = 'moderator'
    MEMBER = 'member'


class User(AbstractUser):
    role = models.CharField(max_length=250, choices=UserRole.choices, default=UserRole.MEMBER)

    username = None
    email = models.EmailField(unique=True, verbose_name='email')
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)
    phone_num = models.CharField(max_length=35, verbose_name='номер телефона', **NULLABLE)
    country = models.CharField(max_length=150, verbose_name='страна', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []