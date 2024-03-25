@testgorilla
Feature:
  As an User
  I want to open browser
  Navigate into TestGorilla exam
  And validate some UI elements of the page

Background:
  Given open browser

@smoke
Scenario: Validate question text
  When navigate into exam page
  Then question text is 'What type of dependency should you set between these two tasks?'

