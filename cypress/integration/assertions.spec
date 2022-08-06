describe('Assertions', () => {
  beforeEach(() => {
    cy.visit('/automation-practice-form')
  })

  afterEach(() => {
    cy.visit('/')
  })

  it('Assertion 1', () => {
    cy.url().should('include', 'demoqa.com')
    // cy.get('#firstName').should('be.visible').should('have.attr', 'placeholder', 'First Name')
    cy.get('#firstName').should('be.visible').and('have.attr', 'placeholder', 'First Name')
  }) 

  it('Assertion 2', () => {
    cy.get('#lastName').then((element) => {
      expect(element).to.be.contain('')
      expect(element).to.have.length(1)
      expect(element).to.have.attr('placeholder', 'Last Name')
      expect(element).to.have.text('')
      expect(element).to.be.visible
    })
  }) 

  it('Assertion 3', () => {
    cy.get('#firstName').then((element) => {
      assert.equal(element.attr('placeholder'), 'First Name')
    })
  }) 

  // You can use it.only() to test a single test case
})