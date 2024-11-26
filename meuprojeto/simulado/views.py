from django.shortcuts import render, redirect, get_object_or_404
from .forms import SimuladoForm
from django.contrib import messages  # Importa o sistema de mensagens para exibir feedbacks aos usuários
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from .models import Simulado
from django.utils import timezone
from aluno.models import Aluno, ResultadoSimulado
from django.db.models import F
from django.http import HttpResponse

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
def info_simulado(request, simulado_id):
    simulado = get_object_or_404(Simulado, id=simulado_id)
    turma = simulado.turma
    alunos = Aluno.objects.filter(turmas=turma)

    # Obter a opção de ordenação da URL
    sort_option = request.GET.get('sort', 'default')
    if sort_option == 'alfabetica':
        alunos = alunos.order_by('nome_aluno')
    elif sort_option == 'idade':
        alunos = alunos.order_by('data_nascimento')
    elif sort_option == 'ranking':
        alunos = alunos.annotate(rank_score=F('resultadosimulado__nota')).order_by('-rank_score', 'data_nascimento')

    # Buscar resultados dos alunos para esse simulado
    resultados = ResultadoSimulado.objects.filter(simulado=simulado)
    todos_com_nota = len(resultados) == alunos.count()

    # Se todos os alunos tiverem nota, calcular o ranking
    ranking_dict = {}
    if todos_com_nota:
        resultados_ordenados = sorted(resultados, key=lambda x: (-x.nota, x.aluno.data_nascimento))
        for posicao, resultado in enumerate(resultados_ordenados, 1):
            ranking_dict[resultado.aluno.id] = posicao

    # Processando o POST para salvar notas
    if request.method == 'POST':
        # Iterar sobre cada aluno e atualizar as notas se fornecidas
        for aluno in alunos:
            nota = request.POST.get(f'notas_{aluno.id}')
            if nota:
                resultado = resultados.filter(aluno=aluno).first()
                if resultado:
                    resultado.nota = float(nota)  # Atualizando a nota
                    resultado.save()

        # Redirecionar para a página de informações do simulado após salvar as alterações
        return redirect('info_simulado', simulado_id=simulado.id)

    # Construir a lista de alunos com os resultados e o ranking
    alunos_com_resultados = []
    for aluno in alunos:
        resultado = resultados.filter(aluno=aluno).first()
        alunos_com_resultados.append({
            'aluno': aluno,
            'nota': resultado.nota if resultado else None,
            'posicao': ranking_dict.get(aluno.id) if todos_com_nota else None
        })

    return render(request, 'simulado/info_simulado.html', {
        'simulado': simulado,
        'turma': turma,
        'alunos_com_resultados': alunos_com_resultados,
        'todos_com_nota': todos_com_nota,
        'sort_option': sort_option
    })


@login_required
def excluir_simulado(request, simulado_id):
    simulado = get_object_or_404(Simulado, id=simulado_id)

    if request.method == 'POST':  # Garantir que a exclusão é feita via POST
        simulado.delete()
        messages.success(request, "Simulado excluído com sucesso!")
        return redirect('listar_simulados')

    return render(request, 'simulado/excluir_simulado_confirmar.html', {'simulado': simulado})



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
