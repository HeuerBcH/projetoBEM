# Generated by Django 5.1.2 on 2024-10-16 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('aluno', '0002_aluno_turma'),
    ]

    operations = [
        migrations.CreateModel(
            name='Simulado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('data_realizacao', models.DateField()),
                ('alunos_participantes', models.ManyToManyField(related_name='simulados', to='aluno.aluno')),
            ],
        ),
    ]
