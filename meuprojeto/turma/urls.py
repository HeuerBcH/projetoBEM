from django.urls import path
from . import views

urlpatterns = [
    path('criar/', views.criar_turma, name='criar_turma'),
    path('listar/', views.listar_turmas, name='listar_turmas'), 
    path('editar_turma/<int:turma_id>/', views.editar_turma, name='editar_turma'),
    path('excluir_turma/<int:turma_id>/', views.excluir_turma, name='excluir_turma'),
]