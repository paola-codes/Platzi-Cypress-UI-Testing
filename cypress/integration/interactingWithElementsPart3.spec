describe('Interacting with Elements', () => {
  it('Interacting with date pickers', () => {
    cy.visit('https://material.angular.io/components/datepicker/overview') 
    cy.get('datepicker-overview-example')
    .find('input')
    .eq(0)
    .type('11/03/2022')

    cy.get('datepicker-overview-example')
    .find('svg')
    .click()
  })

  it('Interacting with modals', () => {
    cy.visit('/modal-dialogs') 
    cy.get('#showSmallModal').click()
    cy.get('#closeSmallModal').click()
  })

  it('Interacting with pop ups', () => {
    cy.visit('/alerts') 

    /*

    // Option #1 for Confirm
    const stub = cy.stub()
    cy.on('window:confirm', stub)

    cy.get('#confirmButton').click().then(() => {
      expect(stub.getCall(0)).to.be.calledWith('Do you confirm action?')
    })

    // Option #2 for Confirm
    cy.get('#confirmButton').click()
    cy.on('window:confirm', (confirm) => {
      expect(confirm).to.equal('Do you confirm action?')
    })

    cy.contains('You selected Ok').should('exist')

    */

    // Rejecting
    cy.get('#confirmButton').click()
    cy.on('window:confirm', (confirm) => {
      expect(confirm).to.equal('Do you confirm action?')
      return false
    })

    cy.contains('You selected Cancel').should('exist')
  })

  it('Interacting with the tool tips', () => {
    cy.visit('/tool-tips') 
    // Mouseover
    cy.get('#toolTipButton').trigger('mouseover')
    cy.contains('You hovered over the Button').should('exist')
    cy.get('#toolTipButton').trigger('mouseout')
    //Mouseout
    cy.contains('You hovered over the Button').should('not.exist')
  })

  it.only('Interacting with drag and drop', () => {
    cy.visit('/dragabble')
    cy.get('#dragBox')
    .trigger('mousedown', {which:1, pageX:600, pageY:100}) // Selection
    .trigger('mousemove', {which:1, pageX:700, pageY:400}) // Movement
    .trigger('mousedown', {which:1, pageX:700, pageY:400}) // Selection
    .trigger('mousemove', {which:1, pageX:900, pageY:200}) // Movement
    .trigger('mouseup') // De-selection
  })
})
