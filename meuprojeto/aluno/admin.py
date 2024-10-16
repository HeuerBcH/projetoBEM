from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Aluno  # Importe o modelo Aluno

# Registre o modelo Aluno para torná-lo visível no admin
admin.site.register(Aluno)
