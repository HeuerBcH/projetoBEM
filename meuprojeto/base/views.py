from django.shortcuts import render, redirect # Importa funções para renderizar templates e redirecionar
from django.contrib.auth import authenticate, login # Importa funções para autenticar e fazer login de usuários
from . models import Usuario # Importa o modelo Usuario que você criou para representar o perfil do usuário
from django.contrib import messages # Importa o sistema de mensagens para exibir feedbacks aos usuários



def home(request):
    return render(request, 'home.html')

# Função para gerenciar o login de usuários
def login_user(request):

    if request.method == 'POST': # Verifica se o tipo de requisição é do tipo POST (significa que o usuário está enviando dados)
        username1 = request.POST['username'] # Obtém o nome de usuário do formulário
        password1 = request.POST['password']# Obtém a senha do formulário

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
    return render(request, 'cadastro.html')
