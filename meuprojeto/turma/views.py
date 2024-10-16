from django.shortcuts import render, redirect, get_object_or_404
from .forms import TurmaForm
from .models import Turma

def criar_turma(request):
    if request.method == 'POST':
        form = TurmaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_turmas')  # Corrigido o nome aqui
    else:
        form = TurmaForm()
    
    return render(request, 'turma/criar_turma.html', {'form': form})

def listar_turmas(request):
    turmas = Turma.objects.all()  # Busca todas as turmas no banco de dados
    return render(request, 'turma/listar_turmas.html', {'turmas': turmas})

def editar_turma(request, turma_id):
    turma = get_object_or_404(Turma, id=turma_id)
    if request.method == 'POST':
        form = TurmaForm(request.POST, instance=turma)
        if form.is_valid():
            form.save()
            return redirect('lista_turmas')  # Redireciona para a lista de turmas
    else:
        form = TurmaForm(instance=turma)
    return render(request, 'editar_turma.html', {'form': form})

def excluir_turma(request, turma_id):
    turma = get_object_or_404(Turma, id=turma_id)
    if request.method == 'POST':
        turma.delete()
        return redirect('lista_turmas')  # Redireciona para a lista de turmas
    return render(request, 'excluir_turma.html', {'turma': turma})