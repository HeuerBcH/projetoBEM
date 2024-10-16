from django.shortcuts import render, redirect
from .forms import SimuladoForm
from django.contrib import messages  # Importa o sistema de mensagens para exibir feedbacks aos usuários
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from .models import Simulado

def criar_simulado(request):
    if request.method == 'POST':
        form = SimuladoForm(request.POST)
        if form.is_valid():
            simulado = form.save(commit=False)
            simulado.save()
            # Redirecione ou faça algo após salvar
            return redirect('/criar_simulado_pagina/')  # Redirecionar após salvar

        else:
            print(form.errors)  # Verifique os erros do formulário para depuração
    else:
        form = SimuladoForm()

    return render(request, 'simulado/criar_simulado.html', {'form': form})

def criar_simulado_pagina(request):
    return render(request, 'simulado/criar_simulado.html')

def listar_simulados(request):
    simulados = Simulado.objects.all()  # Busca todas as turmas no banco de dados
    return render(request, 'simulado/listar_simulados.html', {'simulados': simulados})
