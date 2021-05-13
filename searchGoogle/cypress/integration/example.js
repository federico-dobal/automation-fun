describe('Search automation keyword on Google and ensure that the first automated process was implemented on 1785', () => {

  it('loads search page', () => {
    //GIVEN: the user visits google page and searches for automation keywork
    cy.visit('https://www.google.com');

    cy.get('input[name="q"]').type('automation{enter}');

    // WHEN: the user clicks on Wikipedia link
    cy.get('[href="https://en.wikipedia.org/wiki/Automation"]> .LC20lb')
    .click();

    // THEN: the year when the first industrial automated process was implemente was in 1785
    cy.get('.mw-parser-output > :nth-child(55)')
      .invoke("text")
      .should("contains", "in 1785, making it the first completely automated");

    // take screenshot of the paragraph
    cy.get('.mw-parser-output > :nth-child(55)').screenshot('first_automated_process_paragraph')
  });

});
