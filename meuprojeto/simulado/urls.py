
from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('criar_simulado_pagina/', views.criar_simulado_pagina, name='criar_simulado_pagina'),
    path('criar_simulado/', views.criar_simulado, name='criar_simulado'),

]