describe('Interacting with Elements', () => {
  it('Click', () => {
    cy.visit('/buttons')  
    // For eq(), the counter starts at 1
    // It allows us to find elements by
    // their index number
    cy.get('button').eq(3).click()
    // Once you do that, you get an id and some inner text
    // perfect to make an assertion
    cy.get('#dynamicClickMessage').should('be.visible').and('contain', 'You have done a dynamic click')
  })
  it('Double Click', () => {
    cy.visit('/buttons')  
    // dblclick() does a double click
    cy.get('#doubleClickBtn').dblclick()
    cy.get('#doubleClickMessage').should('be.visible').and('contain', 'You have done a double click')
  })
  it('Right Click', () => {
    cy.visit('/buttons')  
    // rightclick() does a right click
    cy.get('#rightClickBtn').rightclick()
    cy.get('#rightClickMessage').should('be.visible').and('contain', 'You have done a right click')
  })
  it('Force Click', () => {
    cy.visit('/dynamic-properties') 
    // Here, I call upon a button with a tiemout of 5secs
    // and I am making it 0secs instead
    // Also, since it is disabled, we can use
    // force: true to enable it and be able to click it
    // Normally, avoid forcing stuff, because that is
    // going against normal user flow, lowering the 
    // accuracy of your tests
    cy.get('#enableAfter').click({timeout:0, force: true})
  })
  it('Click by Position', () => {
    cy.visit('/buttons')  
    // You can use a specific location within the element
    cy.get('button').eq(3).parent().parent().click('topRight')
    cy.get('button').eq(3).parent().parent().click('bottomLeft')
    // You can also use coordinates
    cy.get('button').eq(3).parent().parent().click(5,60)
  })
    it('Input type text', () => {
    cy.visit('/automation-practice-form') 
    // Type allows us to type inside an input field
    cy.get('#firstName').type('Paola')
    cy.get('#lastName').type('Sanchez')

    // Option #1 to clean field
    cy.get('#firstName').type('{selectAll}{backspace}')
    cy.get('#firstName').type('Andrea')

    // Option #2 to clean field
    cy.get('#firstName').clear()
  })
})


/*
Other type tools

{backspace} Borra el personaje a la izquierda del cursor.
{del} Borra el personaje a la derecha del cursor.
{downarrow} Mueve el cursor hacia abajo.
{end}	Mueve el cursor al final de la línea.
{enter} Teclea la tecla Intro.
{esc}	Teclea la tecla Escape.
{home} Mueve el cursor al principio de la línea.
{insert} Inserta un personaje a la derecha del cursor.
{leftarrow} Mueve el cursor a la izquierda.
{movetoend} Desplaza el cursor al final del elemento mecanizable.
{movetostart} Desplaza el cursor al inicio del elemento mecanizable.
{pagedown} Se desplaza hacia abajo.
{pageup}  Se desplaza hacia arriba.
{rightarrow} Mueve el cursor a la derecha.
{selectall} Selecciona todo el texto creando un selection range.
{uparrow}	Mueve el cursor hacia arriba.

Another method to clean input field
cy.get(’[data-testid=“ModeEditOutlineIcon”]’)
.type(’{selectall}{backspace}value{enter}’)

*/