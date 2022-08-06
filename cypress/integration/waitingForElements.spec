describe('Waiting for Elements', () => {
  beforeEach(() => {
    cy.visit('https://www.platzi.com/')
  })
  it('Waiting for a defined time', () => {
    cy.wait(5000)
  })
  it('Waiting for an element', () => {
    cy.get('.ButtonLogin-cta', {timeout: 6000})
  })
  it('Waiting for an element and make an assertion', () => {
    // Right way
    cy.get('.ButtonLogin-cta', {timeout: 6000}).should('be.visible')
    
    // Wrong way: 
    // cy.get('.ButtonLogin-cta').should('be.visible', {timeout: 6000})
  })
})

describe('Waiting for Elements', () => {
  beforeEach(() => {
    cy.visit('/')
  })
  it.only('Disable the retry', () => {
    cy.get(':nth-child(3) > :nth-child(1) > .card-body', {timeout: 5000})
    // This is used to validate if an element appears 
    // automatically or not
    cy.get(':nth-child(3) > :nth-child(1) > .card-body', {timeout: 0})
    // Undirect waiting is better for overall performance
    // of your tests
  })
})
