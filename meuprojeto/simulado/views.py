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
    # Recupera o Simulado e a Turma associada
    simulado = get_object_or_404(Simulado, id=simulado_id)
    turma = simulado.turma
    
    # Obtém os alunos da turma em ordem alfabética
    alunos = Aluno.objects.filter(turmas=turma).order_by('nome_aluno')
    
    # Verifica se todos os alunos têm uma nota associada
    resultados = ResultadoSimulado.objects.filter(simulado=simulado)
    todos_com_nota = len(resultados) == alunos.count()
    
    # Se o formulário for submetido com o botão "Finalizar"
    if request.method == 'POST' and 'finalizar' in request.POST:
        for aluno in alunos:
            nota = request.POST.get(f'notas_{aluno.id}')
            if nota:
                # Salva ou atualiza o resultado do aluno
                ResultadoSimulado.objects.update_or_create(
                    simulado=simulado,
                    aluno=aluno,
                    defaults={'nota': float(nota)}
                )
        # Redireciona para atualizar a página e exibir o ranking
        return redirect('info_simulado', simulado_id=simulado_id)

    # Cria um dicionário para armazenar o ranking
    ranking_dict = {}
    if todos_com_nota:
        # Ordena os resultados por nota e atribui posições de ranking
        resultados_ordenados = resultados.order_by('-nota')
        for posicao, resultado in enumerate(resultados_ordenados, 1):
            ranking_dict[resultado.aluno.id] = posicao

    # Cria a lista de alunos com seus resultados e o ranking
    alunos_com_resultados = []
    for aluno in alunos:
        resultado = resultados.filter(aluno=aluno).first()
        alunos_com_resultados.append({
            'aluno': aluno,
            'nota': resultado.nota if resultado else None,
            'posicao': ranking_dict.get(aluno.id) if todos_com_nota else None  # Pega a posição do ranking
        })

    # Passa os dados para o template
    return render(request, 'simulado/info_simulado.html', {
        'simulado': simulado,
        'turma': turma,
        'alunos_com_resultados': alunos_com_resultados,
        'todos_com_nota': todos_com_nota
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
