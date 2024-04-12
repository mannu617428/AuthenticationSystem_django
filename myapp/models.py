from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('regular_user', 'Regular User'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='regular_user')
    # user_permissions = models.ManyToManyField('Permissions')

# class Permission(models.Model):
#     name = models.CharField(max_length = 100)

