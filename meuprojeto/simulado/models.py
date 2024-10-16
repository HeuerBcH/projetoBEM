from django.db import models

class Simulado(models.Model):
    nome = models.CharField(max_length=100)
    data_realizacao = models.DateField()
    alunos_participantes = models.ManyToManyField('aluno.Aluno', related_name='simulados')

    def __str__(self):
        return self.nome
