from django.shortcuts import render, redirect  # Importa funções para renderizar templates e redirecionar
from django.contrib.auth import authenticate, login, logout  # Importa funções para autenticar e fazer login de usuários
from .models import Usuario  # Importa o modelo Usuario que você criou para representar o perfil do usuário
from aluno.models import Aluno  # Importe o modelo Aluno do app aluno
from django.contrib import messages  # Importa o sistema de mensagens para exibir feedbacks aos usuários
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist

@login_required
def home(request):
    return render(request, 'home.html')

# Função para gerenciar o login de usuários
from django.core.exceptions import ObjectDoesNotExist


def login_user(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username1 = request.POST['username']
        password1 = request.POST['password']

        user = authenticate(request, username=username1, password=password1)
        if user is not None:
            try:
                usuario_atual = Usuario.objects.get(user=user)
            except ObjectDoesNotExist:
                # Mensagem de erro aparece apenas se o perfil não for encontrado
                messages.error(request, "Perfil de usuário não encontrado.")
                return redirect('login')
            
            # Faz login e redireciona se tudo estiver correto
            login(request, user)
            return redirect('home')
        else:
            # Mensagem de erro só aparece em caso de falha de login
            messages.error(request, "Nome de usuário ou senha incorretos.")
            return redirect('login')
    else:
        return render(request, 'login.html', {})

# Função para gerenciar o cadastro de usuários
def cadastro_user(request):
    # Verifica se o usuário já está autenticado
    if request.user.is_authenticated:
        return redirect('home')  # Redireciona para a página inicial

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Verifica se o usuário já existe
        if User.objects.filter(username=username).exists():
            messages.error(request, "Esse nome de usuário já está em uso.")
            return redirect('cadastro')

        # Cria o usuário
        user = User.objects.create_user(username=username, password=password)

        # Cria o perfil do usuário
        usuario = Usuario(user=user)
        usuario.save()

        messages.success(request, "Cadastro realizado com sucesso! Você já pode fazer login.")
        return redirect('login')  # Redireciona para a página de login
    else:
        return render(request, 'cadastro.html', {})
    
def logout_user(request):
    logout(request)  # Faz o logout do usuário
    # Mensagem de sucesso após logout
    messages.success(request, "Você foi desconectado com sucesso.")
    return redirect('login')

def entrar(request):
    # Se o usuário já estiver autenticado, redireciona para a home
    if request.user.is_authenticated:
        return redirect('home')  # Redireciona para a página inicial

    return render(request, 'entrar.html')

def home(request):
    return render(request, 'home.html')  # Ou o nome do template correspondente