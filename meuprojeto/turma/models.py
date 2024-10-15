from django.db import models


# Create your models here.

class Turma(models.Model):
    nome = models.CharField(max_length=100)
    horario = models.FloatField()
    dias = models.CharField(max_length=100)

    def __str__(self):
        return self.nome