# Generated by Django 5.1.2 on 2024-10-16 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aluno', '0005_remove_aluno_user_aluno_email_responsavel_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='email_responsavel',
            field=models.EmailField(max_length=254, verbose_name='Email do Responsável'),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='nome_aluno',
            field=models.CharField(max_length=100, verbose_name='Nome do Aluno'),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='nome_responsavel',
            field=models.CharField(max_length=100, verbose_name='Nome do Responsável'),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='numero_responsavel',
            field=models.CharField(max_length=15, verbose_name='Número do Responsável'),
        ),
    ]
