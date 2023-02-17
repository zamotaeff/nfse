from django.contrib.auth.models import AbstractUser
from django.db import models

from providers.models import Provider


class User(AbstractUser):
    provider = models.ForeignKey(
        Provider,
        on_delete=models.CASCADE,
        related_name='staffs',
        null=True
    )

    REQUIRED_FIELDS = ['email',
                       'first_name',
                       'last_name',
                       'password']

    def __str__(self):
        return self.username
