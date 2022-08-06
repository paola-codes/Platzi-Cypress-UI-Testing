describe('Interacting with Elements', () => {
  it('Checkboxs and radio buttons', () => {
    cy.visit('/automation-practice-form') 
    //Clicking radio buttons
    // Option #1 to access radio btn inside label
    // cy.get('#gender-radio-1').click({force: true})

    // Using 'force' is not good, it ignores user flow

    // You can also use check instead of click
    //cy.get('#gender-radio-1').check({force: true})

    // Option #2 to access radio btn inside label
    cy.get('label[for="gender-radio-1"]').click()
    // This is the best way!

    // Clicking checkboxes
    //cy.get('label[for="hobbies-checkbox-1"]').click()
    cy.get('#hobbies-checkbox-1').check({force:true})
    cy.get('#hobbies-checkbox-1').uncheck({force:true})
  })
  it('Extracting Information', function() {
    cy.visit('/automation-practice-form') 
    // If you have looong selectors, you can assign
    // a new key name with .as(), example is below
    cy.get('#firstName').as('name')
    cy.get('@name').type('Paola')

    // Since I just typed Paola in the text field
    // let's check that with an assertion
    cy.get('@name').then(($name) => {
      expect($name.val()).to.equal('Paola')
    })

    cy.get('@name').invoke('val').should('equal', 'Paola')
    cy.get('@name').invoke('val').as('globalName')
  })
  // Use regular function structures, not arrow
  // function structures, everytime you want to
  // share information between functions
  it('Share Information', function() {
    cy.visit('/automation-practice-form') 
    cy.get('#firstName').type(this.globalName)
  })
  it('Interacting with dropdowns', () => {
    cy.visit('https://itera-qa.azurewebsites.net/home/automation')  
    // Get by index number
    cy.get('.custom-select').select(10)
    // Get by value and assert the result
    // In this case, the value is a number, and
    // it is the same as the index number
    cy.get('.custom-select').select('3').should('have.value','3')
    // You can also get the text inside, and check if 
    // the text matches its value
    cy.get('.custom-select').select('Greece').should('have.value','4')
  })
  it('Interacting with dropdowns (dynamic)', () => {
    cy.visit('https://react-select.com/home')  
    
    // type(' ') triggers dropdown to open
    cy.get('#react-select-6-input').type(' ')

    /*
    // This allows us to loop through each option
    // and if we land on 'red', we click it
    // This is perfect when we don't know the index
    // we want, only the text
    cy.get('#react-select-6-listbox')
      .children()
      .children()
      .each(($el, index, $list) => {
        if($el.text() === 'Red'){
          // $el.on('click')
          $el.click()
        }
      })
    */

    // Here, you can select an option based on their
    // index, in case you know it
    cy.get('#react-select-6-option-2').click()
  })
  it.only('Interacting with tables', () => {
    cy.visit('https://w3schools.com/html/html_tables.asp')  
    // Lets get the table, each th, and console.log
    // the text of each of them with an each loop
    cy.get('#customers').find('th').each(($el) => {
      cy.log($el.text())
    })

    /*

    // Use first to check a text
    cy.get('#customers')
    .find('th')
    .first()
    .invoke('text')
    .should('equal', 'Company')
    
    // Use eq to check a text
    cy.get('#customers')
    .find('th')
    .eq(2)
    .invoke('text')
    .should('equal', 'Country')

    */

    // Assert length of certain element groups
    cy.get('#customers').find('tr').should('have.length', 7)
    
    // Obtain a text via index numbers
    cy.get('#customers').find('tr').eq(2)
    .find('td').eq(2).invoke('text')
    .should('equal', 'Mexico')

    cy.get('#customers').find('tr').eq(2)
    .find('td').eq(2).then($el => {
      const cellText = $el.text()
      expect(cellText).to.equal('Mexico')
    })
  })
})
