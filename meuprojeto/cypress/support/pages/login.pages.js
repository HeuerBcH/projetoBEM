const INPUT_LOGIN = '#email'
const INPUT_PASSWORD = '#password'
const BUTTON_ENVIAR = '#btnEntrar' 

Cypress.Commands.add('login', (nome, senha) => {
    cy.get(INPUT_LOGIN).type(nome)
    cy.get(INPUT_PASSWORD).type(senha)
    cy.get(BUTTON_ENVIAR).click()
})