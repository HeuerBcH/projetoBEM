from django.shortcuts import render, redirect
from .forms import SimuladoForm
from django.contrib import messages  # Importa o sistema de mensagens para exibir feedbacks aos usuários
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist

def criar_simulado(request):
    if request.method == 'POST':
        form = SimuladoForm(request.POST)
        if form.is_valid():
            form.save()
            
    else:
        form = SimuladoForm()

    return render(request, 'simulado/criar_simulado.html', {'form': form})

def criar_simulado_pagina(request):
    return render(request, 'simulado/criar_simulado.html')
