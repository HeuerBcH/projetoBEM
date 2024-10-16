from django.db import models
from aluno.models import Aluno  # Certifique-se de que o caminho para o modelo Aluno está correto

class Simulado(models.Model):
    MATERIA_CHOICES = (
        ('portugues', 'Português'),
        ('matematica', 'Matemática'),
    )
    
    nome = models.CharField(max_length=100)
    data_realizacao = models.DateField()
    materia = models.CharField(max_length=20, choices=MATERIA_CHOICES,default= 'portugues')
    alunos_participantes = models.ManyToManyField('aluno.Aluno', related_name='simulados')

    def __str__(self):
        return f"{self.nome} - {self.materia} ({self.data_realizacao})"
