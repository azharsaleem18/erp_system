from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class CustomUser(AbstractUser):
    is_active = models.BooleanField(default=False)  # Requires admin approval

    
    def __str__(self):
        return str(self.username)