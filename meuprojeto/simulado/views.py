from django.shortcuts import render, redirect, get_object_or_404
from .forms import SimuladoForm
from django.contrib import messages  # Importa o sistema de mensagens para exibir feedbacks aos usuários
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from .models import Simulado
from django.utils import timezone
from aluno.models import Aluno, ResultadoSimulado

@login_required
def criar_simulado(request):
    if request.method == 'POST':
        form = SimuladoForm(request.POST)
        if form.is_valid():
            simulado = form.save(commit=False)
            simulado.save()
            # Alterar para redirecionar usando o nome da URL
            return redirect('listar_simulados')  # Usando o nome da URL

        else:
            print(form.errors)  # Verifique os erros do formulário para depuração
    else:
        form = SimuladoForm()

    return render(request, 'simulado/criar_simulado.html', {'form': form})


def listar_simulados(request):
    # Busca todos os simulados, ordenando pela data de início
    simulados = Simulado.objects.all().order_by('data_inicio')

    # Separa os simulados futuros e passados
    simulados_futuros = [simulado for simulado in simulados if simulado.data_inicio >= timezone.now()]
    simulados_passados = [simulado for simulado in simulados if simulado.data_inicio < timezone.now()]

    # Passa as listas de simulados para o template
    return render(request, 'simulado/listar_simulados.html', {
        'simulados_futuros': simulados_futuros,
        'simulados_passados': simulados_passados,
        'now': timezone.now()  # Para passar a data atual, se necessário
    })

@login_required
def excluir_simulado(request, simulado_id):
    simulado = get_object_or_404(Simulado, id=simulado_id)

    if request.method == 'POST':  # Garantir que a exclusão é feita via POST
        simulado.delete()
        messages.success(request, "Simulado excluído com sucesso!")
        return redirect('listar_simulados')

    return render(request, 'simulado/excluir_simulado_confirmar.html', {'simulado': simulado})

@login_required
def info_simulado(request, simulado_id):
    # Recupera o Simulado baseado no ID
    simulado = get_object_or_404(Simulado, id=simulado_id)
    
    # Recupera a turma associada ao simulado
    turma = simulado.turma
    
    # Obtém todos os alunos da turma do simulado
    alunos = Aluno.objects.filter(turmas=simulado.turma).order_by('colocacao_geral')
    
    # Obtém os resultados (notas) dos alunos para o simulado
    resultados = ResultadoSimulado.objects.filter(simulado=simulado).order_by('-nota')
    
    # Cria uma lista de alunos com seus resultados e posições
    alunos_com_resultados = []
    for posicao, resultado in enumerate(resultados, 1):
        alunos_com_resultados.append({
            'aluno': resultado.aluno,
            'nota': resultado.nota,
            'posicao': posicao  # Calcula a posição dinamicamente
        })
    
    # Passa os dados para o template
    return render(request, 'simulado/info_simulado.html', {
        'simulado': simulado,
        'turma': turma,
        'alunos_com_resultados': alunos_com_resultados
    })



def editar_simulado(request, simulado_id):
    simulado = get_object_or_404(Simulado, id=simulado_id)

    if request.method == 'POST':
        form = SimuladoForm(request.POST, instance=simulado)
        if form.is_valid():
            form.save()
            return redirect('listar_simulados')  # Redireciona para a lista de simulados
    else:
        form = SimuladoForm(instance=simulado)

    return render(request, 'simulado/editar_simulado.html', {
        'form': form,
        'simulado': simulado,
    })
