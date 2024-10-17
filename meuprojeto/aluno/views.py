from django.shortcuts import render, redirect
from .forms import AlunoForm
from .models import Aluno

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
