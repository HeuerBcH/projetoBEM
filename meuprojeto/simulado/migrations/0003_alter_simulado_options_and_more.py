# Generated by Django 5.1.2 on 2024-10-16 22:23

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simulado', '0002_simulado_materia'),
        ('turma', '0004_alter_turma_alunos'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='simulado',
            options={'verbose_name': 'Simulado', 'verbose_name_plural': 'Simulados'},
        ),
        migrations.RemoveField(
            model_name='simulado',
            name='alunos_participantes',
        ),
        migrations.RemoveField(
            model_name='simulado',
            name='data_realizacao',
        ),
        migrations.AddField(
            model_name='simulado',
            name='data_inicio',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data e Hora de Início'),
        ),
        migrations.AddField(
            model_name='simulado',
            name='turma',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='turma.turma', verbose_name='Turma'),
        ),
        migrations.AlterField(
            model_name='simulado',
            name='materia',
            field=models.CharField(choices=[('matematica', 'Matemática'), ('portugues', 'Português')], max_length=20, verbose_name='Matéria'),
        ),
        migrations.AlterField(
            model_name='simulado',
            name='nome',
            field=models.CharField(max_length=100, verbose_name='Nome do Simulado'),
        ),
    ]