from django.urls import path
from . import views

urlpatterns = [
    path('criar/', views.criar_turma, name='criar_turma'),
    path('listar/', views.listar_turmas, name='listar_turmas'),  # URL para listar turmas
]