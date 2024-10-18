from django.db import models
import datetime
from django.contrib.auth.models import User

# Create your models here.

class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username