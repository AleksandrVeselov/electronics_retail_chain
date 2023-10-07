from django.contrib.auth.models import AbstractUser
from django.db import models


class Employee(AbstractUser):
    """Модель сотрудника"""

    email = models.EmailField(unique=True, verbose_name='email')

    name = models.CharField(max_length=100, verbose_name='Имя')  # Имя сотрудника
    surname = models.CharField(max_length=100, verbose_name='Фамилия')  # Фамилия сотрудника
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.name} {self.surname}'