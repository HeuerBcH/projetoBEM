from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Aluno(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    matricula = models.CharField(max_length=20, unique=True)
    data_nascimento = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.username