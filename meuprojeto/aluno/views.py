from django.shortcuts import render, redirect
from .forms import AlunoForm
from .models import Aluno
from django.shortcuts import get_object_or_404

def adicionar_aluno(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_alunos')  # Redireciona após salvar
    else:
        form = AlunoForm()
    return render(request, 'adicionar_aluno.html', {'form': form})


def listar_alunos(request):
    alunos = Aluno.objects.all()
    return render(request, 'listar_alunos.html', {'alunos': alunos})

def editar_aluno(request, pk):
    aluno = Aluno.objects.get(pk=pk)
    
    if request.method == 'POST':
        form = AlunoForm(request.POST, instance=aluno)
        if form.is_valid():
            form.save()
            return redirect('listar_alunos')  # Redireciona após salvar
    else:
        form = AlunoForm(instance=aluno)
    
    return render(request, 'editar_aluno.html', {'form': form, 'aluno': aluno})

def excluir_aluno(request, pk):
    aluno = get_object_or_404(Aluno, pk=pk)
    if request.method == 'POST':
        aluno.delete()
        return redirect('listar_alunos')  # Redireciona para a lista de alunos após a exclusão
    return render(request, 'excluir_aluno.html', {'aluno': aluno})