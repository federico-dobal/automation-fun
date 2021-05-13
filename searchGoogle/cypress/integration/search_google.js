describe('Search automation keyword on Google and ensure that the first automated process was implemented on 1785', () => {

  it('loads search page, search automation keyword, very conditions and take screenshot', () => {
    //GIVEN: the user visits Google page and searches for automation keywork
    cy.visit('https://www.google.com');

    cy.get('input[name="q"]').type('automation{enter}');

    // WHEN: the user clicks on Wikipedia link
    cy.get('[href="https://en.wikipedia.org/wiki/Automation"]> .LC20lb').click();

    // THEN: verify the year when the first industrial automated process was implemented
    cy.get('.mw-parser-output > :nth-child(55)')
      .invoke("text")
      .then((text) => {

        // Not very explicit, verify by long string comparisson
        expect(text).to.include('in 1785, making it the first completely automated')

        // More explicit, only check the date, still string comparison but only 4 characters long
        const retrieved_date = text.split('Oliver Evans in')[1].split(',')[0].trim();
        expect(retrieved_date).to.eq('1785')
      });

    // take paragraph screenshot
    cy.get('.mw-parser-output > :nth-child(55)').screenshot('first_automated_process_paragraph')
  });

});
