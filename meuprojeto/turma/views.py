from django.shortcuts import render, redirect, get_object_or_404
from .forms import TurmaForm
from .models import Turma
from django.contrib import messages

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
        form = TurmaForm(request.POST, instance=turma)  # Passa a instância da turma
        if form.is_valid():
            form.save()
            messages.success(request, 'Turma editada com sucesso!')
            return redirect('listar_turmas')
    else:
        form = TurmaForm(instance=turma)  # Preenche o formulário com os dados da turma

    return render(request, 'turma/editar_turma.html', {'form': form, 'turma': turma})



def excluir_turma(request, turma_id):
    turma = get_object_or_404(Turma, id=turma_id)
    if request.method == 'POST':
        turma.delete()
        messages.success(request, 'Turma excluída com sucesso!')  # Mensagem de sucesso
        return redirect('listar_turmas')
    else:
        return redirect('listar_turmas')  # Ou exibir uma mensagem de alerta

def info_turma(request, turma_id):
    turma = get_object_or_404(Turma, id=turma_id)
    return render(request, 'turma/info_turma.html', {'turma': turma})
