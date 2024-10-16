from django.contrib.auth.models import User
from django.db import models

class Aluno(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    matricula = models.CharField(max_length=20, unique=True)
    data_nascimento = models.DateField(null=True, blank=True)
    turmas = models.ManyToManyField('turma.Turma', related_name='alunos_turmas')  # Alterado para evitar conflito

    def __str__(self):
        return self.user.username
