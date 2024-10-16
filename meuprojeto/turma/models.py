from django.db import models
from django.utils import timezone

# Create your models here.

class Turma(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da Turma")
    horario_inicio = models.TimeField(verbose_name="Horário de Início", default='06:00')  # Valor padrão
    horario_fim = models.TimeField(verbose_name="Horário de Fim", default='07:00')  # Valor padrão
    dias = models.CharField(max_length=100, verbose_name="Dias da Semana")  
    professor = models.CharField(max_length=100, verbose_name="Professor Responsável", blank=True, null=True)
    alunos = models.ManyToManyField('aluno.Aluno', related_name='turmas_matriculadas')

    def __str__(self):
        return f"{self.nome} ({self.horario_inicio} - {self.horario_fim})"

    class Meta:
        verbose_name = "Turma"
        verbose_name_plural = "Turmas"
