from django.contrib.auth.models import AbstractUser, Permission, Group
from django.db import models
import uuid

ROLES_CHOICES = [
    ('USER', 'User'),
    ('ADMIN', 'Admin'),
    ('OWNER FIELD', 'OWNER FIELD'),
]


class CustomUser(AbstractUser):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    email = models.EmailField(max_length=200, blank=False, null=False)
    password = models.CharField(max_length=200, blank=False, null=False)
    image = models.ImageField(upload_to="userimage/", blank=True, null=True)
    roles = models.CharField(max_length=20, choices=ROLES_CHOICES, default='USER')

    def __str__(self) -> str:
        return self.username 
    
