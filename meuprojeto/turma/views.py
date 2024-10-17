from django.shortcuts import render, redirect
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
