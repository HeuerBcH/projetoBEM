from django.shortcuts import render, redirect # Importa funções para renderizar templates e redirecionar
from django.contrib.auth import authenticate, login, logout # Importa funções para autenticar e fazer login de usuários
from . models import Usuario # Importa o modelo Usuario que você criou para representar o perfil do usuário
from django.contrib import messages # Importa o sistema de mensagens para exibir feedbacks aos usuários
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request, 'home.html')

# Função para gerenciar o login de usuários
def login_user(request):

    # Verifica se o usuário já está autenticado
    if request.user.is_authenticated:
        return redirect('home')  # Redireciona para a página inicial

    if request.method == 'POST': # Verifica se o tipo de requisição é do tipo POST (significa que o usuário está enviando dados)
        username1 = request.POST['username'] # Obtém o nome de usuário do formulário
        password1 = request.POST['password'] # Obtém a senha do formulário

        user = authenticate(request, username=username1, password=password1) # Autentica as informações de login
        if user is not None: 
            login(request, user) # Faz o login

            usuario_atual = Usuario.objects.get(user=user) # Obtem o perfil do usuário associado ao usuário autenticado
            return redirect('home') # Redireciona para a página inicial após o login
        
        else:
            # Se a autenticação falhar, exibe uma mensagem de erro
            messages.error(request, ("Ocorreu um erro, se você não possuir uma conta, registre-se, caso contrário, verifique suas informações."))
            return redirect('login')
    else:
        # Se a requisição não for do tipo POST, renderiza a página de login sem erros
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
    logout(request) # Faz o logout do usuário
    messages.success(request, "Você foi desconectado com sucesso.")
    return redirect('login')
