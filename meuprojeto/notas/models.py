from django.db import models

class Nota(models.Model):
    aluno = models.ForeignKey('aluno.Aluno', on_delete=models.CASCADE, related_name='notas')
    portugues = models.DecimalField(max_digits=5, decimal_places=2)
    matematica = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"Notas de {self.aluno.user.username}"

class Ranking(models.Model):
    aluno = models.OneToOneField('aluno.Aluno', on_delete=models.CASCADE, related_name='ranking')
    posicao = models.IntegerField()

    def __str__(self):
        return f"Ranking de {self.aluno.user.username}: {self.posicao}"
