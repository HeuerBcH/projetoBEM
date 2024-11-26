from django.urls import path
from .views import adicionar_aluno, listar_alunos, editar_aluno, excluir_aluno
from . import views

urlpatterns = [
    path('adicionar/', adicionar_aluno, name='adicionar_aluno'),
    path('listar/', listar_alunos, name='listar_alunos'),
    path('editar/<int:pk>/', editar_aluno, name='editar_aluno'),
    path('excluir/<int:pk>/', excluir_aluno, name='excluir_aluno'),
    
    
]