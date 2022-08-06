describe('Types of Localizers', () => {
  beforeEach(() => {
    cy.visit('/automation-practice-form')
  })
  
  it('Obtain via a tag', () => {
    // cy.once('uncaught:exception', () => false);
    cy.get('input')
  })

  it('Obtain via an attribute', () => {
    cy.get('[placeholder="First Name"]')
  })

  it('Obtain via an attribute and a tag', () => {
    cy.get('input[placeholder="First Name"]')
  })

  it('Obtain via an id', () => {
    cy.get('#firstName')
  })

  it('Obtain via a class', () => {
    // Original class name is mr-sm-2 form-control
    // For cypress, turn spaces into periods
    cy.get('.mr-sm-2.form-control')
  })

  it('Using "contains"', () => {
    cy.contains('Reading')
    cy.contains('.header-wrapper','Widgets')
  })

  it('Using "parent"', () => {
    //Obtaining the parent element
    cy.get('input[placeholder="First Name"]').parent()

    //Obtaining the parent elements
    cy.get('input[placeholder="First Name"]').parents()
    cy.get('input[placeholder="First Name"]').parents().find('label')
    cy.get('form').find('label')

    // Never do cy.find('label'), because
    // find() needs to be concatenated
  })
})
