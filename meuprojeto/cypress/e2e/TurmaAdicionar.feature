#utf-8
#language: pt

Funcionalidade: Adicionar uma nova turma
    Cenário: Adicionar turma com sucesso
        Dado que estou logado num perfil de usuário
        E eu esteja na página "home"
        Quando eu acessar a página de adicionar uma nova turma
        E enviar o formulário com as informações da nova turma
        Então a nova turma deve ser visível na página de listagem de turmas