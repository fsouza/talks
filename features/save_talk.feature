Feature: Save a talk
    In order to get organize
    As a speaker
    I want to registry my talks

    Scenario: Saving a talk
        Given I am logged in the system
        When I navigate to the new talk page
        And fill the title field with "Django: The web framework for perfectionists with deadlines"
        And fill the description field with "My first talk about Django, I really like this"
        And fill the date field with "01/25/2010"
        And click on the button Save talk
        Then I should be redirected to the home page
        And I should see "Django: The web framework for perfectionists with deadlines" on the screen
