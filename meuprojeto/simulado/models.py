from django.db import models
from django.utils import timezone
from turma.models import Turma  # Importa o modelo Turma

class Simulado(models.Model):
    MATERIA_CHOICES = [
        ('matematica', 'Matemática'),
        ('portugues', 'Português'),
    ]

    nome = models.CharField(max_length=100, verbose_name="Nome do Simulado")
    materia = models.CharField(max_length=20, choices=MATERIA_CHOICES, verbose_name="Matéria")
    data_inicio = models.DateTimeField(default=timezone.now, verbose_name="Data e Hora de Início")
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Turma")  # Define o valor padrão para 'turma'

    def __str__(self):
        return f"{self.nome} - {self.materia} - {self.turma}"

    class Meta:
        verbose_name = "Simulado"
        verbose_name_plural = "Simulados"
