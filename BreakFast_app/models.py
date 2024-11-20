from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    #username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'  # Use email as the username
    REQUIRED_FIELDS = []  # No required fields for creating a user

    def __str__(self):
        return self.email
    
    # def __str__(self):
    #     return self.username
