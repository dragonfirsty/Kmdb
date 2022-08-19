from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    username = models.CharField(max_length=20,unique=True)
    email = models.EmailField(unique=True,max_length=127)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birthdate = models.DateField()
    bio = models.TextField(blank=True, null=True)
    is_critic = models.BooleanField(blank=True, default=False)
    updated_at = models.DateTimeField(auto_now=True)


    REQUIRED_FIELDS = ["email","first_name","last_name","birthdate"]