// {browser: 'chrome'} determines broser preference
// at the test level, before running the tests.

// {browser: '!firefox'} says that this test should
// be ran in every browser except for firefox.

describe('Navigation', {browser: 'chrome'}, () => {
  it('Navigate to our first page', () => {
    cy.visit('https://www.platzi.com/')
  })
  
  it('Reload page', () => {
    cy.reload()
  })

  it('Forcefully reload page', () => {
    cy.visit('https://www.google.com/')
    // Reload without cache
    cy.reload(true)
  })

  it('Navigate backwards', () => {
    cy.visit('https://www.google.com/')
    cy.visit('https://www.google.com/search?q=platzi&ei=3fbrYr7aOtuAkvQPtoOdwAg&ved=0ahUKEwj-vJG90K35AhVbgIQIHbZBB4gQ4dUDCA4&uact=5&oq=platzi&gs_lcp=Cgdnd3Mtd2l6EAMyEQguEIAEELEDEIMBEMcBENEDMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEOgcIABBHELADOgsILhCABBDHARCvAToHCAAQgAQQCjoHCAAQsQMQCjoKCAAQsQMQgwEQCjoECAAQCkoECEEYAEoECEYYAFCoBlipCGDFC2gBcAF4AIAB7QGIAcMDkgEDMi0ymAEAoAEByAEIwAEB&sclient=gws-wiz')
    // cy.go('back')
    cy.go(-1)
  })

  it.only('Navigate forward', () => {
    cy.visit('https://www.google.com/')
    cy.visit('https://www.google.com/search?q=platzi&ei=3fbrYr7aOtuAkvQPtoOdwAg&ved=0ahUKEwj-vJG90K35AhVbgIQIHbZBB4gQ4dUDCA4&uact=5&oq=platzi&gs_lcp=Cgdnd3Mtd2l6EAMyEQguEIAEELEDEIMBEMcBENEDMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEOgcIABBHELADOgsILhCABBDHARCvAToHCAAQgAQQCjoHCAAQsQMQCjoKCAAQsQMQgwEQCjoECAAQCkoECEEYAEoECEYYAFCoBlipCGDFC2gBcAF4AIAB7QGIAcMDkgEDMi0ymAEAoAEByAEIwAEB&sclient=gws-wiz')
    cy.go('back')
    // cy.go(1)
    cy.go('forward')
  })
})