const INPUT_NOME = '#username'
const INPUT_SENHA = '#password1'
const BUTTON_SUBMIT = '#registerButton' 


Cypress.Commands.add('cadastrar', (nome, senha) => {
    cy.get(INPUT_NOME).type(nome)
    cy.get(INPUT_SENHA).type(senha)
    cy.get(BUTTON_SUBMIT).click()
})