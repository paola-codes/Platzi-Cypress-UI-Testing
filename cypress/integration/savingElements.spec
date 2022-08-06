describe('Saving Elements', () => {
  beforeEach(() => {
    cy.visit('/automation-practice-form')
  })
  it('Repetition', () => {
    // Input parents
    cy.get('input[placeholder="First Name"]').parent()
    cy.get('input[placeholder="First Name"]').parents()
    cy.get('input[placeholder="First Name"]').parents().find('label')
    
    // Form labels
    cy.get('form').find('label')
  })

  it('Avoid Repetition', () => {
    // Input parents
    cy.get('input[placeholder="First Name"]').parents('form').then((form) => {
      const inputs = form.find('input')
      const divs = form.find('div')
      const labels = form.find('label')

      // Assertions
      expect(inputs.length).to.eq(15)
      expect(divs.length).to.eq(70)
      expect(labels.length).to.eq(16)

      // 'inputs', 'divs', and 'label' come from 
      // 'form' on line 14. This is a JQuery element;
      // therefore, we cannot use the chainers
      // from cypress, unless we wrap them, example:
      cy.wrap(inputs).should('have.length', 15)

      // console.log('I am the length', inputs.length)

      // This helps you see the results of everything
      // on the browsers' console
      // debugger

      // This helps you see the result of a specific
      // test on the terminal
      cy.task('log', inputs.length)

      // Option to console log in the browser
      cy.log('I am the length', inputs.length)
    })

    // Form labels
    cy.get('form').find('label')

    // Pause execution
    // cy.pause()

    // Directly console log a test
    // Look for S.fn.init(1) on console of browser
    cy.get('input[placeholder="First Name"]').then(console.log)

    // See debug on browser console
    cy.get('input[placeholder="First Name"]').debug()
  })
})