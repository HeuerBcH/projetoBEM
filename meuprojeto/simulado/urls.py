
from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views


urlpatterns = [

    path('criar_simulado/', views.criar_simulado, name='criar_simulado'),
    path('listar_simulados/', views.listar_simulados, name='listar_simulados'),
    path('excluir_simulado/<int:simulado_id>/', views.excluir_simulado, name='excluir_simulado'),
    path('info_simulado/<int:simulado_id>/', views.info_simulado, name='info_simulado'),
    path('editar_simulado/<int:simulado_id>/', views.editar_simulado, name='editar_simulado'),

]