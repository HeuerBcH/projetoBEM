from django.db import models
from django.utils import timezone
from simulado.models import Simulado

class Aluno(models.Model):
    nome_aluno = models.CharField(max_length=100, verbose_name="Nome do Aluno")
    matricula = models.BooleanField(default=True, verbose_name="Matriculado")
    data_nascimento = models.DateField(null=True, blank=True, verbose_name="Data de Nascimento")
    turmas = models.ManyToManyField('turma.Turma', related_name='alunos_turmas')
    nome_responsavel = models.CharField(max_length=100, verbose_name="Nome do Responsável")
    numero_responsavel = models.CharField(max_length=15, verbose_name="Número do Responsável")
    email_responsavel = models.EmailField(max_length=254, verbose_name="Email do Responsável")
    colocacao_geral = models.IntegerField(default=0, verbose_name="Colocação Geral")

    def __str__(self):
        return self.nome_aluno

class ResultadoSimulado(models.Model):
    simulado = models.ForeignKey(Simulado, on_delete=models.CASCADE)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    nota = models.FloatField()

    def __str__(self):
        return f"Resultado {self.aluno.nome_aluno} - {self.simulado.nome}"