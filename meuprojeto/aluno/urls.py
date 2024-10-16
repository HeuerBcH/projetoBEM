from django.urls import path
from .views import adicionar_aluno, listar_alunos

urlpatterns = [
    path('adicionar/', adicionar_aluno, name='adicionar_aluno'),
    path('listar/', listar_alunos, name='listar_alunos'),
]