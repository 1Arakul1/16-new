from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # Дополнительные поля
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    is_premium = models.BooleanField(default=False)
    # Новое поле:
    address = models.CharField(max_length=255, blank=True, null=True)

    # Добавьте related_name для полей groups и user_permissions
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_name="custom_user_set",
        related_query_name="user",
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="custom_user_set",
        related_query_name="user",
    )


    def __str__(self):
        return self.username